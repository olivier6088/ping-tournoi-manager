from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .models import Player, Table, Tournament


class TournamentFlowTests(TestCase):
    def _formset_management_data(self, total):
        return {
            "tableaux-TOTAL_FORMS": str(total),
            "tableaux-INITIAL_FORMS": "0",
            "tableaux-MIN_NUM_FORMS": "1",
            "tableaux-MAX_NUM_FORMS": "1000",
        }

    def test_create_tournament_persists_and_redirects(self):
        url = reverse("create_tournament")
        data = {
            "nom": "Open de Saint-Denis",
            "date": "2024-05-01",
            "lieu": "Saint-Denis",
            "nb_tables": 12,
            "max_simples": 2,
            "max_doubles": 1,
            "action": "save",
            "tableaux-0-nom": "Tableau A",
            "tableaux-0-classement_max": 1200,
        }
        data.update(self._formset_management_data(total=1))

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        tournament = Tournament.objects.get(nom="Open de Saint-Denis")
        self.assertRedirects(response, reverse("tournament_detail", args=[tournament.pk]))
        self.assertEqual(tournament.tableaux.count(), 1)
        self.assertEqual(tournament.tableaux.first().classement_max, 1200)

    def test_import_players_with_table_assignment(self):
        tournament = Tournament.objects.create(
            nom="Coupe locale",
            date="2024-06-10",
            lieu="Saint-Pierre",
            nb_tables=8,
            max_simples=2,
            max_doubles=1,
        )
        table = Table.objects.create(
            tournament=tournament, nom="Tableau A", classement_max=1300
        )

        csv_content = (
            "licence;nom;prenom;sexe;club;points;date_naissance;tableau\n"
            "9999;Doe;Jane;F;Club Test;900;1990-01-01;Tableau A\n"
        )
        upload = SimpleUploadedFile(
            "joueurs.csv", csv_content.encode("utf-8"), content_type="text/csv"
        )

        response = self.client.post(
            reverse("tournament_detail", args=[tournament.pk]),
            data={"fichier": upload},
        )

        self.assertEqual(response.status_code, 302)
        player = Player.objects.get(licence="9999", tournament=tournament)
        self.assertEqual(player.tableau, table)
