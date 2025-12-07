# Generated manually to introduce Tournoi model and link it to Tableau
from django.db import migrations, models
import django.db.models.deletion
from django.db.models import Q


class Migration(migrations.Migration):

    dependencies = [
        ("competitions", "0002_alter_tableau_min_points"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tournoi",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nom", models.CharField(max_length=120)),
                ("date", models.DateField()),
                ("lieu", models.CharField(blank=True, max_length=120)),
                ("nb_tables", models.PositiveIntegerField(default=16)),
                ("contraintes", models.JSONField(blank=True, default=dict)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Tournoi",
                "verbose_name_plural": "Tournois",
                "ordering": ["-date", "nom"],
                "unique_together": {("nom", "date")},
                "constraints": [
                    models.CheckConstraint(
                        name="tournoi_nb_tables_positive",
                        condition=Q(("nb_tables__gte", 1)),
                    )
                ],
            },
        ),
        migrations.AddField(
            model_name="tableau",
            name="tournoi",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tableaux",
                to="competitions.tournoi",
            ),
        ),
    ]
