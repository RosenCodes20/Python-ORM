from django.core.exceptions import ValidationError


def validate_menu_categories(value):
    if "Appetizers" not in value or "Main Course" not in value or "Desserts" not in value:
        raise ValidationError('The menu must include each of the categories "Appetizers", "Main Course", "Desserts".')