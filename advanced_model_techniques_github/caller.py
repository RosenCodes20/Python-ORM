import os
import django
from django.core.exceptions import ValidationError

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# Keep the data from the previous exercise, so you can reuse it

from main_app.models import RegularRestaurantReview, Restaurant, MenuReview, Menu
print(Restaurant.objects.first().menu_set.last().menureview_set.first().reviewer_name)
# Create queries within functions
