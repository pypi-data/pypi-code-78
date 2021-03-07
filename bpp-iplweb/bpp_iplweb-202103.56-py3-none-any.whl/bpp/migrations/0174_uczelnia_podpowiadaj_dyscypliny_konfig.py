# Generated by Django 2.1.7 on 2019-08-23 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0173_auto_20190812_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='uczelnia',
            name='podpowiadaj_dyscypliny',
            field=models.BooleanField(default=True, help_text='W sytuacji gdy to pole ma wartość "PRAWDA", system będzie podpowiadał dyscyplinę\n        naukową dla powiązania rekordu wydawnictwa i autora w sytuacji, gdy autor ma na dany rok\n        określoną tylko jedną dyscyplinę. W sytuacji przypisania dla autora dwóch dyscyplin na dany rok, \n        pożądaną dyscyplinę będzie trzeba wybrać ręcznie, niezależnie od ustawienia tego pola. '),
        ),
    ]
