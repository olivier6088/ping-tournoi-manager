from django.contrib import admin
from .models import Club, Inscription, Joueur, Tableau, Tournoi


@admin.register(Tournoi)
class TournoiAdmin(admin.ModelAdmin):
    list_display = ("nom", "date", "lieu", "nb_tables")
    search_fields = ("nom", "lieu")
    list_filter = ("date",)

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ("nom", "code", "ville")
    search_fields = ("nom", "code", "ville")

@admin.register(Joueur)
class JoueurAdmin(admin.ModelAdmin):
    list_display = ("licence", "prenom", "nom", "club", "points", "sexe", "age")
    list_filter = ("sexe", "club")
    search_fields = ("licence", "nom", "prenom")
    ordering = ("-points", "nom")

@admin.register(Tableau)
class TableauAdmin(admin.ModelAdmin):
    list_display = ("libelle", "date", "min_points", "max_points", "is_double", "mixte", "capacite")
    list_filter = ("date", "is_double", "mixte")
    search_fields = ("libelle",)

@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ("joueur", "tableau", "partenaire", "statut", "created_at")
    list_filter = ("statut", "tableau__date", "tableau__is_double")
    search_fields = ("joueur__nom", "joueur__prenom", "joueur__licence", "partenaire__nom", "partenaire__prenom")
