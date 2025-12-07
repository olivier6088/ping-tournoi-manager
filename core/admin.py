from django.contrib import admin

from .models import Player, Table, Tournament


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ("nom", "date", "lieu", "nb_tables")
    search_fields = ("nom", "lieu")
    list_filter = ("date",)


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ("nom", "classement_max", "tournament")
    list_filter = ("tournament",)
    search_fields = ("nom", "tournament__nom")


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        "licence",
        "prenom",
        "nom",
        "club",
        "points",
        "tournament",
        "tableau",
    )
    list_filter = ("tournament", "tableau")
    search_fields = ("licence", "nom", "prenom", "club")
