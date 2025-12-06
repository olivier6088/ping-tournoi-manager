from django import forms

class UploadCSVForm(forms.Form):
    fichier = forms.FileField(
        label="Fichier CSV",
        help_text="CSV encodé UTF-8 ; séparateur ; ou ,"
    )