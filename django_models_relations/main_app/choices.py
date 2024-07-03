from django.db import models


class GradeChoice(models.TextChoices):
    A = "A", "A"
    B = "B", "B"
    C = "C", "C"
    D = "D", "D"
    F = "F", "F"


class CarChoices(models.TextChoices):
    BMW = "BMW", "BMW"
    MERCEDES = "Mercedes", "Mercedes"
    SKODA = "Skoda", "Skoda"
    MAZDA = "Mazda", "Mazda"
    AUDI = "Audi", "Audi"
    SEAT = "Seat", "Seat"