from django.shortcuts import render
from .forms import UploadCSVForm
import csv, io

def upload_joueurs(request):
    preview = None
    headers = None
    error = None

    if request.method == "POST":
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.cleaned_data["fichier"]
            try:
                # décodage (UTF-8 par défaut)
                data = f.read().decode("utf-8", errors="replace")
                # détection du séparateur ; ou ,
                sniffer = csv.Sniffer()
                dialect = sniffer.sniff(data.splitlines()[0] if data else "a;b", delimiters=";,")
                reader = csv.reader(io.StringIO(data), dialect)
                rows = list(reader)

                if rows:
                    headers = rows[0]
                    preview = rows[1:11]  # 10 lignes
                else:
                    error = "Fichier vide."
            except Exception as e:
                error = f"Impossible de lire le fichier: {e}"
    else:
        form = UploadCSVForm()

    return render(
        request,
        "competitions/import_joueurs.html",
        {"form": form, "headers": headers, "preview": preview, "error": error},
    )
