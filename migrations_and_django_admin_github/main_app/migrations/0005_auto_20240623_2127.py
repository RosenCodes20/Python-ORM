# Generated by Django 5.0.4 on 2024-06-23 18:27
import random

from django.db import migrations


class Migration(migrations.Migration):

    def add_barcode(apps, schema_editor):
        product = apps.get_model("main_app", "Product")
        all_barcodes = product.objects.all()

        random_barcodes = random.sample(
            range(100_000_000, 1_000_000_000),
            len(all_barcodes)
        )

        for product, barcode in zip(all_barcodes, random_barcodes):
            product.barcode = barcode
            product.save()

    def reverse_adding_barcode(apps, schema_editor):
        product = apps.get_model("main_app", "Product")
        all_barcodes = product.objects.all()

        for product in all_barcodes:
            product.barcode = 0
            product.save()

    dependencies = [
        ('main_app', '0004_alter_product_category_alter_product_supplier'),
    ]

    operations = [
        migrations.RunPython(add_barcode, reverse_code=reverse_adding_barcode)
    ]