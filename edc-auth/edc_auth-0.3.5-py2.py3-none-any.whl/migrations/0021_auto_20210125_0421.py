# Generated by Django 3.1.5 on 2021-01-25 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edc_auth", "0020_auto_20210120_0005"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="export_format",
            field=models.CharField(
                blank=True,
                choices=[("CSV", "CSV")],
                default="CSV",
                help_text="Note: requires export permissions",
                max_length=25,
                null=True,
                verbose_name="Export format",
            ),
        ),
    ]
