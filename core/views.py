import csv
import io
from datetime import datetime

from django.contrib import messages
from django.forms import formset_factory
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PlayerImportForm, TableForm, TournamentForm
from .models import Player, Table, Tournament


def home(request):
    return render(request, "core/home.html")


def create_tournament(request):
    preview = None
    TableFormSet = formset_factory(TableForm, extra=1, min_num=1, validate_min=True)

    form = TournamentForm(request.POST or None)
    table_formset = TableFormSet(request.POST or None, prefix="tableaux")

    if request.method == "POST" and form.is_valid() and table_formset.is_valid():
        table_data = [table for table in table_formset.cleaned_data if table]
        if request.POST.get("action") == "save":
            tournament = form.save()
            for tableau in table_data:
                Table.objects.create(tournament=tournament, **tableau)
            messages.success(
                request,
                "Tournoi enregistré. Vous pouvez maintenant importer des joueurs.",
            )
            return redirect("tournament_detail", pk=tournament.pk)

        preview = {**form.cleaned_data, "tableaux": table_data}

    return render(
        request,
        "core/create_tournament.html",
        {"form": form, "table_formset": table_formset, "preview": preview},
    )


def _parse_date(value):
    if not value:
        return None

    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    raise ValueError("format de date invalide")


def _parse_players_csv(file_obj, tables_by_name):
    content = file_obj.read().decode("utf-8-sig")
    if not content:
        return [], ["Le fichier est vide."]

    first_line = content.splitlines()[0]
    delimiter = ";" if ";" in first_line else ","

    reader = csv.DictReader(io.StringIO(content), delimiter=delimiter)
    required_fields = {
        "licence",
        "nom",
        "prenom",
        "sexe",
        "club",
        "points",
        "date_naissance",
        "tableau",
    }

    missing = required_fields - set(reader.fieldnames or [])
    if missing:
        return [], [f"Colonnes manquantes : {', '.join(sorted(missing))}."]

    parsed = []
    errors = []
    for index, row in enumerate(reader, start=2):
        try:
            licence = row.get("licence", "").strip()
            nom = row.get("nom", "").strip()
            prenom = row.get("prenom", "").strip()
            sexe = row.get("sexe", "").strip().upper()
            club = row.get("club", "").strip()
            points_raw = row.get("points", "0").replace(" ", "")
            date_value = row.get("date_naissance", "").strip()
            tableau_name = row.get("tableau", "").strip()

            if not licence or not nom or not prenom or sexe not in {"M", "F"}:
                raise ValueError("Champs obligatoires manquants ou sexe invalide")

            tableau = None
            if tableau_name:
                tableau = tables_by_name.get(tableau_name.lower())
                if not tableau:
                    raise ValueError(
                        f"tableau inconnu : {tableau_name}. Utilisez les noms existants."
                    )

            parsed.append(
                {
                    "licence": licence,
                    "nom": nom,
                    "prenom": prenom,
                    "sexe": sexe,
                    "club": club,
                    "points": int(points_raw or 0),
                    "date_naissance": _parse_date(date_value) if date_value else None,
                    "tableau": tableau,
                }
            )
        except Exception as exc:  # noqa: BLE001
            errors.append(f"Ligne {index}: {exc}")

    return parsed, errors


def tournament_detail(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    tables = list(tournament.tableaux.all())
    players = tournament.players.select_related("tableau").all()
    import_form = PlayerImportForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and import_form.is_valid():
        tables_by_name = {table.nom.lower(): table for table in tables}
        players_data, errors = _parse_players_csv(
            import_form.cleaned_data["fichier"], tables_by_name
        )

        if errors:
            for error in errors:
                messages.error(request, error)
        else:
            for data in players_data:
                Player.objects.update_or_create(
                    tournament=tournament,
                    licence=data["licence"],
                    defaults={
                        "nom": data["nom"],
                        "prenom": data["prenom"],
                        "sexe": data["sexe"],
                        "club": data["club"],
                        "points": data["points"],
                        "date_naissance": data["date_naissance"],
                        "tableau": data["tableau"],
                    },
                )

            messages.success(
                request,
                f"{len(players_data)} joueurs importés et affectés à leurs tableaux.",
            )
            return redirect("tournament_detail", pk=tournament.pk)

    return render(
        request,
        "core/tournament_detail.html",
        {
            "tournament": tournament,
            "tables": tables,
            "players": players,
            "import_form": import_form,
        },
    )
