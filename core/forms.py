from django import forms


COMMON_INPUT_CLASSES = "w-full rounded-lg border border-slate-300 bg-white px-3 py-2 shadow-sm focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 dark:bg-slate-800 dark:border-slate-700 dark:text-white"


class TournamentForm(forms.Form):
    nom = forms.CharField(
        label="Nom du tournoi",
        max_length=120,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Open de Saint-Paul",
                "class": COMMON_INPUT_CLASSES,
            }
        ),
    )
    date = forms.DateField(
        label="Date",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": COMMON_INPUT_CLASSES,
            }
        ),
    )
    lieu = forms.CharField(
        label="Lieu",
        max_length=120,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Gymnase Nelson",
                "class": COMMON_INPUT_CLASSES,
            }
        ),
    )
    nb_tables = forms.IntegerField(
        label="Nombre de tables",
        min_value=1,
        initial=16,
        widget=forms.NumberInput(
            attrs={
                "class": COMMON_INPUT_CLASSES,
            }
        ),
    )
    max_simples = forms.IntegerField(
        label="Nombre maximum de simples par joueur",
        min_value=0,
        initial=2,
        widget=forms.NumberInput(
            attrs={
                "class": COMMON_INPUT_CLASSES,
            }
        ),
    )
    max_doubles = forms.IntegerField(
        label="Nombre maximum de doubles par joueur",
        min_value=0,
        initial=1,
        widget=forms.NumberInput(
            attrs={
                "class": COMMON_INPUT_CLASSES,
            }
        ),
    )


class TableForm(forms.Form):
    nom = forms.CharField(
        label="Nom du tableau",
        max_length=80,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Tableau A", "class": COMMON_INPUT_CLASSES
            }
        ),
    )
    classement_max = forms.IntegerField(
        label="Classement maximal autorisé",
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "class": COMMON_INPUT_CLASSES,
                "placeholder": "Ex. 1299",
            }
        ),
    )
