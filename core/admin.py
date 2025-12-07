from django.contrib import admin

from .models import Player, Table, Tournament


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ("nom", "date", "lieu", "nb_tables")
    search_fields = ("nom", "lieu")
    list_filter = ("date",)


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ("nom", "code", "classement_max", "tournament")
    list_filter = ("tournament",)
    search_fields = ("nom", "code", "tournament__nom")


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        "licence",
        "prenom",
        "nom",
        "club",
        "points",
        "tournament",
        "tableaux_list",
    )
    list_filter = ("tournament",)
    search_fields = ("licence", "nom", "prenom", "club")
    filter_horizontal = ("tableaux",)

    @admin.display(description="Tableaux")
    def tableaux_list(self, obj):
        return ", ".join(obj.tableaux.values_list("code", flat=True))
