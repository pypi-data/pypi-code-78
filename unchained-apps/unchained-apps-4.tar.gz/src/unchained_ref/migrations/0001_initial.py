# Generated by Django 3.1.4 on 2020-12-30 12:36

from django.db import migrations, models
import django.db.models.deletion
import unchained_utils.v0.base_classes


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name_en', models.CharField(max_length=100)),
                ('name_ar', models.CharField(max_length=100)),
            ],
            options={
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name_en', models.CharField(max_length=100)),
                ('name_ar', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=100, unique=True)),
                ('name_en', models.CharField(max_length=100)),
                ('name_ar', models.CharField(blank=True, max_length=100, null=True)),
                ('country', unchained_utils.v0.base_classes.LooseForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='unchained_ref.country')),
            ],
            options={
                'unique_together': {('key', 'country')},
            },
        ),
    ]
