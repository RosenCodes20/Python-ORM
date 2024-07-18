import os
import django
from django.db.models import Count, Max, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Review, Article


#from dummy import populate_model_with_data


def get_authors(search_name=None, search_email=None):
    result = []

    if search_name is not None and search_email is not None:
        authors = Author.objects.filter(full_name__contains=search_name, email__contains=search_email).order_by(
            "-full_name")

    elif search_name is not None and search_email is None:
        authors = Author.objects.filter(full_name__contains=search_name).order_by("-full_name")

    elif search_name is None and search_email is not None:
        authors = Author.objects.filter(email__contains=search_email).order_by("-full_name")

    else:
        return ""

    for author in authors:
        result.append(
            f"Author: {author.full_name}, email: {author.email}, status: {'Banned' if author.is_banned else 'Not Banned'}")

    return "\n".join(result)


def get_top_publisher():
    top_author = Author.objects.annotate(num_articles=Count('article')).order_by("-num_articles", "email").first()

    if not Article.objects.all():
        return ""

    if top_author:
        return f"Top Author: {top_author.full_name} with {top_author.article_set.count()} published articles."


def get_top_reviewer():
    top_author_with_reviews_all = Author.objects.annotate(num_reviews=Count('review')).order_by("-num_reviews", "email")

    if not Review.objects.all():
        return ""

    if top_author_with_reviews_all:
        top_author_with_reviews = top_author_with_reviews_all.first()
        return f"Top Reviewer: {top_author_with_reviews.full_name} with {top_author_with_reviews.review_set.count()} published reviews."


def get_latest_article():
    if not Article.objects.all():
        return ""

    last_article = Article.objects.all().annotate(avg_rating=Avg("review__rating")).last()
    full_names = [a.full_name for a in last_article.authors.all().order_by("full_name")]
    return f"The latest article is: {last_article.title}. Authors: {', '.join(full_names)}. Reviewed: {last_article.review_set.count()} times. Average Rating: {last_article.avg_rating or 0:.2f}."


def get_top_rated_article():
    top_article = Article.objects.annotate(avg_rating=Avg("review__rating")).order_by("-avg_rating", "title").first()

    if not Review.objects.all():
        return ""

    return f"The top-rated article is: {top_article.title}, with an average rating of {top_article.avg_rating:.2f}, reviewed {top_article.review_set.count()} times."


def ban_author(email=None):
    if not Author.objects.filter(email=email) or email is None:
        return "No authors banned."

    author = Author.objects.get(email=email)
    author.is_banned = True
    author.save()
    reviews_count = author.review_set.count()
    author.review_set.all().delete()
    return f"Author: {author.full_name} is banned! {reviews_count} reviews deleted."


print(get_latest_article())