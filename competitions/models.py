from datetime import date

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils import timezone


class Tournoi(models.Model):
    nom = models.CharField(max_length=120)
    date = models.DateField()
    lieu = models.CharField(max_length=120, blank=True)
    nb_tables = models.PositiveIntegerField(default=16)
    contraintes = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "nom"]
        unique_together = [("nom", "date")]
        verbose_name = "Tournoi"
        verbose_name_plural = "Tournois"
        constraints = [
            models.CheckConstraint(
                name="tournoi_nb_tables_positive",
                condition=Q(nb_tables__gte=1),
            ),
        ]

    def __str__(self):
        return f"{self.nom} ({self.date})"


class Club(models.Model):
    code = models.CharField(max_length=10, unique=True)
    nom = models.CharField(max_length=100)
    ville = models.CharField(max_length=80, blank=True)

    class Meta:
        ordering = ["nom"]
        verbose_name = "Club"
        verbose_name_plural = "Clubs"

    def __str__(self):
        return f"{self.nom} ({self.code})"


class Joueur(models.Model):
    SEXE_CHOICES = [("M", "Homme"), ("F", "Femme")]
    licence = models.CharField(max_length=12, unique=True)
    nom = models.CharField(max_length=80)
    prenom = models.CharField(max_length=80)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    date_naissance = models.DateField(null=True, blank=True)
    club = models.ForeignKey(Club, on_delete=models.PROTECT, related_name="joueurs")
    points = models.PositiveIntegerField(default=500)

    class Meta:
        ordering = ["-points", "nom", "prenom"]
        verbose_name = "Joueur"
        verbose_name_plural = "Joueurs"
        indexes = [
            models.Index(fields=["licence"]),
            models.Index(fields=["points"]),
        ]
        constraints = [
            # points FFTT ≥ 500
            models.CheckConstraint(
                name="joueur_points_min_500",
                condition=Q(points__gte=500),
            ),
            # date de naissance réaliste si renseignée (>= 1920)
            models.CheckConstraint(
                name="joueur_dna_valide_si_renseignee",
                condition=Q(date_naissance__isnull=True) | Q(date_naissance__gte=date(1920, 1, 1)),
            ),
        ]

    @property
    def age(self):
        if not self.date_naissance:
            return None
        today = date.today()
        return today.year - self.date_naissance.year - (
            (today.month, today.day) < (self.date_naissance.month, self.date_naissance.day)
        )

    def __str__(self):
        return f"{self.prenom} {self.nom} [{self.points}]"


class Tableau(models.Model):
    tournoi = models.ForeignKey(
        "Tournoi",
        on_delete=models.CASCADE,
        related_name="tableaux",
        null=True,
        blank=True,
    )
    libelle = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    min_points = models.PositiveIntegerField(default=500)
    max_points = models.PositiveIntegerField(default=4000)
    is_double = models.BooleanField(default=False)
    mixte = models.BooleanField(default=False)
    capacite = models.PositiveIntegerField(default=64)

    class Meta:
        ordering = ["date", "libelle"]
        verbose_name = "Tableau"
        verbose_name_plural = "Tableaux"
        constraints = [
            # capacité ≥ 0
            models.CheckConstraint(
                name="tableau_capacite_positive",
                condition=Q(capacite__gte=0),
            ),
            # bornes cohérentes : 0 ≤ min ≤ max ≤ 4000
            models.CheckConstraint(
                name="tableau_bornes_points_coherentes",
                condition=Q(min_points__gte=0) & Q(max_points__lte=4000) & Q(min_points__lte=models.F("max_points")),
            ),
        ]

    def __str__(self):
        p = f" [{self.min_points}-{self.max_points}]"
        cap = f" (cap {self.capacite})" if self.capacite else ""
        tournoi = f" — {self.tournoi.nom}" if self.tournoi else ""
        return f"{self.libelle}{p}{cap}{tournoi}"

class Inscription(models.Model):
    """
    Représente la participation d’un joueur à un tableau (simple ou double).
    - Pas de doublon joueur/tableau.
    - Si tableau.is_double -> partenaire requis.
    - Si tableau simple -> partenaire interdit.
    """

    STATUTS = [
        ("PENDING", "En attente"),
        ("CONFIRMED", "Confirmée"),
        ("CHECKED_IN", "Pointée"),
        ("WITHDRAWN", "Forfait"),
    ]

    joueur = models.ForeignKey(
        "Joueur",
        on_delete=models.CASCADE,
        related_name="inscriptions",
    )
    tableau = models.ForeignKey(
        "Tableau",
        on_delete=models.CASCADE,
        related_name="inscriptions",
    )
    partenaire = models.ForeignKey(
        "Joueur",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="inscriptions_partenaire",
    )
    statut = models.CharField(max_length=12, choices=STATUTS, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [("joueur", "tableau")]
        ordering = ["-created_at"]
        verbose_name = "Inscription"
        verbose_name_plural = "Inscriptions"
        
    def clean(self):
        # règle C : pas de partenaire en simple
        if self.tableau and not self.tableau.is_double and self.partenaire:
            raise ValidationError("Pas de partenaire autorisé pour un tableau de simple.")
        
        # règle D : partenaire requis en double
        if self.tableau and self.tableau.is_double and not self.partenaire:
            raise ValidationError("Un partenaire est requis pour un tableau de double.")
        
        # règle E : partenaire différent du joueur
        if self.partenaire and self.partenaire_id == self.joueur_id:
            raise ValidationError("Le partenaire ne peut pas être le même joueur.")
        
        # règle F : max 2 simples + 1 double sur la même date
        if self.tableau:
            jour = self.tableau.date
            qs = Inscription.objects.filter(
                joueur_id=self.joueur_id,
                tableau__date=jour,
            )
            if self.pk:
                qs = qs.exclude(pk=self.pk)  # ne pas se compter soi-même en édition

            simples = qs.filter(tableau__is_double=False).count()
            doubles = qs.filter(tableau__is_double=True).count()

            # inclure l'inscription en cours dans le décompte futur
            simples_future = simples + (0 if self.tableau.is_double else 1 if self.partenaire is None else 1)
            doubles_future = doubles + (1 if self.tableau.is_double else 0)

            if simples_future > 2:
                raise ValidationError("Un joueur ne peut pas participer à plus de 2 tableaux de simples le même jour.")
            if doubles_future > 1:
                raise ValidationError("Un joueur ne peut pas participer à plus d’un tableau de double le même jour.")

    
    def save(self, *args, **kwargs):
        self.full_clean()  # force l'appel à clean() avant enregistrement
        return super().save(*args, **kwargs)

    # def clean(self):
    #     """Validation Python (ORM) exécutée avant save() et dans l’admin."""
    #     if not self.tableau:
    #         return

    #     if self.tableau.is_double and not self.partenaire:
    #         raise ValidationError("Un partenaire est requis pour un tableau de double.")
    #     if not self.tableau.is_double and self.partenaire:
    #         raise ValidationError("Pas de partenaire autorisé pour un tableau de simple.")
    #     if self.partenaire and self.partenaire == self.joueur:
    #         raise ValidationError("Le partenaire ne peut pas être le même joueur.")

    # def save(self, *args, **kwargs):
    #     """Force la validation ORM avant l’enregistrement."""
    #     self.full_clean()
    #     return super().save(*args, **kwargs)

    def __str__(self):
        if self.tableau.is_double and self.partenaire:
            return f"{self.joueur} + {self.partenaire} → {self.tableau}"
        return f"{self.joueur} → {self.tableau}"
