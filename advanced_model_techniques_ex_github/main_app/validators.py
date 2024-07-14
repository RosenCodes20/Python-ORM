from django.core.exceptions import ValidationError


def name_validator(value):
    for letter in value:
        if not letter.isalpha() and not letter.isspace():
            raise ValidationError("Name can only contain letters and spaces")

