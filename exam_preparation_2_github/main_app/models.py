from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.managers import CustomManager


class TennisPlayer(models.Model):
    full_name = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(120)
        ]
    )

    birth_date = models.DateField()

    country = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(100)
        ]
    )

    ranking = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(300)
        ]
    )

    is_active = models.BooleanField(
        default=True
    )

    objects = CustomManager()


class Tournament(models.Model):
    class SurfaceChoices(models.TextChoices):
        NOT_SELECTED = "Not Selected", "Not Selected"
        CLAY = "Clay", "Clay"
        GRASS = "Grass", "Grass"
        HARD_COURT = "Hard Court", "Hard Court"

    name = models.CharField(
        max_length=150,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(150)
        ],
        unique=True
    )

    location = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(100)
        ]
    )

    prize_money = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    start_date = models.DateField()

    surface_type = models.CharField(
        max_length=12,
        choices=SurfaceChoices.choices,
        default="Not Selected",
        validators=[
            MaxLengthValidator(12)
        ]
    )


class Match(models.Model):
    score = models.CharField(
        max_length=100,
        validators=[
            MaxLengthValidator(100)
        ]
    )

    summary = models.TextField(
        validators=[
            MinLengthValidator(5)
        ]
    )

    date_played = models.DateTimeField()

    tournament = models.ForeignKey(
        to=Tournament,
        on_delete=models.CASCADE,
        related_name="tournaments"
    )

    players = models.ManyToManyField(
        to=TennisPlayer,
        related_name="players_played"
    )

    winner = models.ForeignKey(
        to=TennisPlayer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="winners"
    )

    class Meta:
        verbose_name_plural = "Matches"
