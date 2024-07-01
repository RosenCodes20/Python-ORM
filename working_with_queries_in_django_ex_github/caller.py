import os
from typing import List

import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

#from dummy import populate_model_with_data
from main_app.models import ArtworkGallery, Laptop
from main_app.choices import LaptopBrandChoices, OperationSystemChoice


def show_highest_rated_art():
    highest_rated_art = ArtworkGallery.objects.order_by("-rating", "id").first()

    return f"{highest_rated_art.art_name} is the highest-rated art with a {highest_rated_art.rating} rating!"


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery):
    ArtworkGallery.objects.bulk_create(
        [
            first_art,
            second_art
        ]
    )


def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop():
    highest_paid_laptop = Laptop.objects.order_by("-price", "-id").first()

    return f"{highest_paid_laptop.brand} is the most expensive laptop available for {highest_paid_laptop.price}$!"


def bulk_create_laptops(args: List[Laptop]):
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage():
    (Laptop.objects.filter(
        brand__in=(LaptopBrandChoices.ASUS, LaptopBrandChoices.LENOVO
                     )
    )
     .update(storage=512)
     )


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=(
        LaptopBrandChoices.ACER,
        LaptopBrandChoices.APPLE,
        LaptopBrandChoices.DELL
    )).update(memory=16)


def update_operation_systems():
    (Laptop.objects.filter(
        brand=LaptopBrandChoices.ASUS
    )
     .update(operation_system=OperationSystemChoice.WINDOWS))

    Laptop.objects.filter(
        brand=LaptopBrandChoices.APPLE
    ).update(operation_system=OperationSystemChoice.MAC_OS)

    Laptop.objects.filter(
        brand__in=(
            LaptopBrandChoices.DELL,
            LaptopBrandChoices.ACER
        )
    ).update(operation_system=OperationSystemChoice.LINUX)

    Laptop.objects.filter(
        brand=LaptopBrandChoices.LENOVO
    ).update(operation_system=OperationSystemChoice.CHROME_OS)


def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()


delete_inexpensive_laptops()