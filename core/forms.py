from django import forms
from django.core.validators import FileExtensionValidator

from .models import Table, Tournament


COMMON_INPUT_CLASSES = "w-full rounded-lg border border-slate-300 bg-white px-3 py-2 shadow-sm focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 dark:bg-slate-800 dark:border-slate-700 dark:text-white"


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = [
            "nom",
            "date",
            "lieu",
            "nb_tables",
            "max_simples",
            "max_doubles",
        ]
        widgets = {
            "nom": forms.TextInput(
                attrs={
                    "placeholder": "Ex: Tournoi des Aiglons d'Orient",
                    "class": COMMON_INPUT_CLASSES,
                }
            ),
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": COMMON_INPUT_CLASSES,
                }
            ),
            "lieu": forms.TextInput(
                attrs={
                    "placeholder": "Ex: Gymnase des 2 Canons",
                    "class": COMMON_INPUT_CLASSES,
                }
            ),
            "nb_tables": forms.NumberInput(
                attrs={
                    "class": COMMON_INPUT_CLASSES,
                }
            ),
            "max_simples": forms.NumberInput(
                attrs={
                    "class": COMMON_INPUT_CLASSES,
                }
            ),
            "max_doubles": forms.NumberInput(
                attrs={
                    "class": COMMON_INPUT_CLASSES,
                }
            ),
        }


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ["nom", "code", "classement_max"]
        widgets = {
            "nom": forms.TextInput(
                attrs={
                    "placeholder": "Ex. Tableau A",
                    "class": COMMON_INPUT_CLASSES,
                }
            ),
            "code": forms.TextInput(
                attrs={
                    "placeholder": "Ex. A1200",
                    "class": COMMON_INPUT_CLASSES,
                    "pattern": "[A-Za-z0-9_-]+",
                    "title": "Utilisez des lettres, chiffres, tirets ou underscores",
                }
            ),
            "classement_max": forms.NumberInput(
                attrs={
                    "class": COMMON_INPUT_CLASSES,
                    "placeholder": "Ex. 1299",
                    "min": 500,
                }
            ),
        }


class PlayerImportForm(forms.Form):
    fichier = forms.FileField(
        label="Fichier CSV des joueurs",
        validators=[FileExtensionValidator(["csv"])],
        widget=forms.ClearableFileInput(
            attrs={"class": "block w-full text-sm text-slate-700 dark:text-slate-200"}
        ),
        help_text=(
            "Colonnes requises : licence, nom, prenom, sexe, club, points, "
            "date_naissance et tableaux (identifiants séparés par |)."
        ),
    )
