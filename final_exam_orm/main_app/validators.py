from django.core.exceptions import ValidationError


def only_digits_validator(value):
    if not value.isdigit():
        raise ValidationError("This field must contain only digits!")