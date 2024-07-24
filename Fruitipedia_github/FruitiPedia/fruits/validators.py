from django.core.exceptions import ValidationError


def only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")