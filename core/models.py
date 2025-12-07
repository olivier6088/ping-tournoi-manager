from django.db import models


class Tournament(models.Model):
    nom = models.CharField(max_length=120)
    date = models.DateField()
    lieu = models.CharField(max_length=120, blank=True)
    nb_tables = models.PositiveIntegerField()
    max_simples = models.PositiveIntegerField(default=0)
    max_doubles = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "nom"]

    def __str__(self):
        return self.nom


class Table(models.Model):
    tournament = models.ForeignKey(
        Tournament, related_name="tableaux", on_delete=models.CASCADE
    )
    nom = models.CharField(max_length=80)
    code = models.SlugField(max_length=50)
    classement_max = models.PositiveIntegerField()

    class Meta:
        ordering = ["nom"]
        unique_together = [("tournament", "code")]

    def __str__(self):
        return f"{self.nom} ({self.tournament.nom})"


class Player(models.Model):
    tournament = models.ForeignKey(
        Tournament, related_name="players", on_delete=models.CASCADE
    )
    licence = models.CharField(max_length=20)
    nom = models.CharField(max_length=120)
    prenom = models.CharField(max_length=120)
    sexe = models.CharField(
        max_length=1, choices=[("M", "Masculin"), ("F", "Féminin")]
    )
    club = models.CharField(max_length=120, blank=True)
    points = models.PositiveIntegerField(default=0)
    date_naissance = models.DateField(null=True, blank=True)
    tableaux = models.ManyToManyField(Table, related_name="players", blank=True)

    class Meta:
        ordering = ["nom", "prenom"]
        unique_together = [("tournament", "licence")]

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.licence})"
