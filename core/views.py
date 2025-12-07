from django.shortcuts import render

from .forms import TournamentForm

def home(request):
    return render(request, "core/home.html")


def create_tournament(request):
    preview = None
    form = TournamentForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        preview = form.cleaned_data

    return render(
        request,
        "core/create_tournament.html",
        {"form": form, "preview": preview},
    )
