from django.db import models
from django.db.models import Count


class CustomManager(models.Manager):
    def get_authors_by_article_count(self):
        return self.all().annotate(count_articles=Count("article__id")).order_by("-count_articles", "email")