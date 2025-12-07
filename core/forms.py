from django import forms


class TournamentForm(forms.Form):
    nom = forms.CharField(
        label="Nom du tournoi",
        max_length=120,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Open de Saint-Paul",
                "class": "w-full rounded-lg border border-slate-300 bg-white px-3 py-2 shadow-sm"
                " focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500"
                " dark:bg-slate-800 dark:border-slate-700 dark:text-white",
            }
        ),
    )
    date = forms.DateField(
        label="Date",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "w-full rounded-lg border border-slate-300 bg-white px-3 py-2 shadow-sm"
                " focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500"
                " dark:bg-slate-800 dark:border-slate-700 dark:text-white",
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
                "class": "w-full rounded-lg border border-slate-300 bg-white px-3 py-2 shadow-sm"
                " focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500"
                " dark:bg-slate-800 dark:border-slate-700 dark:text-white",
            }
        ),
    )
    nb_tables = forms.IntegerField(
        label="Nombre de tables",
        min_value=1,
        initial=16,
        widget=forms.NumberInput(
            attrs={
                "class": "w-full rounded-lg border border-slate-300 bg-white px-3 py-2 shadow-sm"
                " focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500"
                " dark:bg-slate-800 dark:border-slate-700 dark:text-white",
            }
        ),
    )
    contraintes = forms.CharField(
        label="Contraintes globales (optionnel)",
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 4,
                "placeholder": "Ex. max 2 simples + 1 double, anti-club activé…",
                "class": "w-full rounded-lg border border-slate-300 bg-white px-3 py-2 shadow-sm"
                " focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500"
                " dark:bg-slate-800 dark:border-slate-700 dark:text-white",
            }
        ),
    )
