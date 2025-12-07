from django.forms import formset_factory
from django.shortcuts import render

from .forms import TableForm, TournamentForm


def home(request):
    return render(request, "core/home.html")


def create_tournament(request):
    preview = None
    TableFormSet = formset_factory(TableForm, extra=0, min_num=1, validate_min=True)

    form = TournamentForm(request.POST or None)
    if request.method == "POST":
        table_formset = TableFormSet(request.POST, prefix="tableaux")
    else:
        table_formset = TableFormSet(prefix="tableaux", initial=[{}])

    if request.method == "POST" and form.is_valid() and table_formset.is_valid():
        preview = {
            **form.cleaned_data,
            "tableaux": [table for table in table_formset.cleaned_data if table],
        }

    return render(
        request,
        "core/create_tournament.html",
        {"form": form, "table_formset": table_formset, "preview": preview},
    )
