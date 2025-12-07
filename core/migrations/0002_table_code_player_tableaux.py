from django.db import migrations, models
from django.utils.text import slugify


def populate_table_codes(apps, schema_editor):
    Table = apps.get_model("core", "Table")

    for table in Table.objects.all():
        base_slug = slugify(table.nom) or f"tableau-{table.pk}"
        code = base_slug[:50]

        siblings = Table.objects.filter(tournament=table.tournament).exclude(pk=table.pk)
        existing = set(siblings.values_list("code", flat=True))
        suffix = 1
        while code in existing:
            suffix += 1
            code = f"{base_slug}-{suffix}"[:50]

        table.code = code
        table.save(update_fields=["code"])


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="table",
            name="code",
            field=models.SlugField(default="", max_length=50),
            preserve_default=False,
        ),
        migrations.RunPython(populate_table_codes, migrations.RunPython.noop),
        migrations.AlterUniqueTogether(
            name="table",
            unique_together={("tournament", "code")},
        ),
        migrations.RemoveField(
            model_name="player",
            name="tableau",
        ),
        migrations.AddField(
            model_name="player",
            name="tableaux",
            field=models.ManyToManyField(blank=True, related_name="players", to="core.table"),
        ),
    ]
