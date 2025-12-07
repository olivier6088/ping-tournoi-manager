# Generated manually to introduce tournament persistence and players import.
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tournament",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nom", models.CharField(max_length=120)),
                ("date", models.DateField()),
                ("lieu", models.CharField(blank=True, max_length=120)),
                ("nb_tables", models.PositiveIntegerField()),
                ("max_simples", models.PositiveIntegerField(default=0)),
                ("max_doubles", models.PositiveIntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-date", "nom"]},
        ),
        migrations.CreateModel(
            name="Table",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nom", models.CharField(max_length=80)),
                ("classement_max", models.PositiveIntegerField()),
                (
                    "tournament",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tableaux",
                        to="core.tournament",
                    ),
                ),
            ],
            options={"ordering": ["nom"]},
        ),
        migrations.CreateModel(
            name="Player",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("licence", models.CharField(max_length=20)),
                ("nom", models.CharField(max_length=120)),
                ("prenom", models.CharField(max_length=120)),
                ("sexe", models.CharField(choices=[("M", "Masculin"), ("F", "Féminin")], max_length=1)),
                ("club", models.CharField(blank=True, max_length=120)),
                ("points", models.PositiveIntegerField(default=0)),
                ("date_naissance", models.DateField(blank=True, null=True)),
                (
                    "tableau",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="players",
                        to="core.table",
                    ),
                ),
                (
                    "tournament",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="players",
                        to="core.tournament",
                    ),
                ),
            ],
            options={"ordering": ["nom", "prenom"], "unique_together": {("tournament", "licence")}},
        ),
    ]
