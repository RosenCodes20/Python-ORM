# Generated by Django 5.0.4 on 2024-06-23 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20240623_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
