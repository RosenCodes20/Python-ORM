import os

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# zip project tar.exe -a -cf project.zip main_app orm_skeleton caller.py manage.py requirements.txt
from main_app.models import VideoGame, BillingInfo, Invoice, Programmer, Project, Technology, Task, Exercise
from django.db.models import Count, Avg, Max

print(VideoGame.objects.values("title").annotate(avg_rating=Max("rating")).order_by("-avg_rating"))
print(VideoGame.objects.values("release_year").annotate(count_of_year=Count("release_year")).order_by("-count_of_year"))
print(Task.objects.values("priority").annotate(count_prioroty=Count("priority")))