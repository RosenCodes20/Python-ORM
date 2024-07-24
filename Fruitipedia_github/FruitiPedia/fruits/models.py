from django.core.validators import MinLengthValidator
from django.db import models

from FruitiPedia.fruits.validators import only_letters_validator


# Create your models here.


class Category(models.Model):
    name = models.CharField(
        max_length=60,
        unique=True
    )

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            only_letters_validator
        ],
        null=False,
        blank=False
    )

    image_url = models.URLField(
        null=False,
        blank=False
    )

    description = models.TextField(
        null=False,
        blank=False
    )

    nutrition = models.TextField(
        null=True,
        blank=True
    )

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
