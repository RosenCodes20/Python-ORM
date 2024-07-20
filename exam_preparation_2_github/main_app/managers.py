from django.db import models
from django.db.models import Count


class CustomManager(models.Manager):
    def get_tennis_players_by_wins_count(self):
        return self.all().annotate(winners_count=Count("winners")).order_by("-winners_count", "full_name")