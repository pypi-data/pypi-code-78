# Generated by Django 3.0.11 on 2021-03-07 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0242_auto_20210307_1110"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autor",
            name="system_kadrowy_id",
            field=models.PositiveIntegerField(
                blank=True,
                db_index=True,
                help_text="Identyfikator cyfrowy, używany do matchowania autora z danymi z systemu kadrowego Uczelni",
                null=True,
                unique=True,
                verbose_name="Identyfikator w systemie kadrowym",
            ),
        ),
    ]
