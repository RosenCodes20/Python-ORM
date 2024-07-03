import os
import random

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import City, Country
from dummy import populate_model_with_data

country = Country.objects.get(name="Bulgaria")

City.objects.filter(country=None).update(country=country)

# Create queries within functions
