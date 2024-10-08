from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator, MaxLengthValidator
from django.db import models

from main_app.managers import CustomManager


class Author(models.Model):
    full_name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(3)
        ]
    )

    email = models.EmailField(
        unique=True
    )

    is_banned = models.BooleanField(
        default=False
    )

    birth_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1990),
            MaxValueValidator(2005)
        ]
    )

    website = models.URLField(
        null=True,
        blank=True
    )

    objects = CustomManager()


class Article(models.Model):
    class CategoryChoices(models.TextChoices):
        TECHNOLOGY = "Technology", "Technology"
        SCIENCE = "Science", "Science"
        EDUCATION = "Education", "Education"

    title = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(200)
        ]
    )

    content = models.TextField(
        validators=[
            MinLengthValidator(10)
        ]
    )

    category = models.CharField(
        max_length=10,
        choices=CategoryChoices.choices,
        validators=[
            MaxLengthValidator(10)
        ],
        default="Technology"
    )

    authors = models.ManyToManyField(
        to=Author
    )

    published_on = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )


class Review(models.Model):
    content = models.TextField(
        validators=[
            MinLengthValidator(10)
        ]
    )

    rating = models.FloatField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
    )

    article = models.ForeignKey(
        to=Article,
        on_delete=models.CASCADE
    )

    published_on = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
