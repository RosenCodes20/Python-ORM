# Generated by Django 5.0.4 on 2024-07-03 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_city_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='country_id',
            new_name='country',
        ),
    ]
