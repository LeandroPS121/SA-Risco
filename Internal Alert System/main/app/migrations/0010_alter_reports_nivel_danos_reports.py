# Generated by Django 5.0.7 on 2024-07-11 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_erifica_area_risco_risco_verifica_area_risco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='nivel_danos_reports',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
