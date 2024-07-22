# Generated by Django 5.0.4 on 2024-07-15 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_match_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournaments', to='main_app.tournament'),
        ),
    ]