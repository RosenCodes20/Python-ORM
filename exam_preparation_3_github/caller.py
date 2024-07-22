import os
import django
from django.db.models import Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Actor, Director, Movie
from decimal import Decimal


# from dummy import populate_model_with_data

# Import your models here
#   tar.exe -a -cf project.zip main_app orm_skeleton caller.py manage.py requirements.txt
# Create queries within functions


def get_directors(search_name=None, search_nationality=None):
    if not Director.objects.all():
        return ""

    result = []

    if search_name is not None and search_nationality is not None:
        directors = Director.objects.filter(full_name__icontains=search_name,
                                            nationality__icontains=search_nationality).order_by("full_name")

    elif search_name is not None and search_nationality is None:
        directors = Director.objects.filter(full_name__icontains=search_name).order_by("full_name")

    elif search_name is None and search_nationality is not None:
        directors = Director.objects.filter(nationality__icontains=search_nationality).order_by("full_name")

    else:
        return ""

    for director in directors:
        result.append(
            f"Director: {director.full_name}, nationality: {director.nationality}, experience: {director.years_of_experience}")

    return "\n".join(result)


def get_top_director():
    if not Director.objects.all():
        return ""

    top_director = Director.objects.annotate(count_of_movies=Count("movie")).order_by("-count_of_movies",
                                                                                      "full_name").first()

    return f"Top Director: {top_director.full_name}, movies: {top_director.count_of_movies}."


def get_top_actor():
    if not Movie.objects.all():
        return ""
    top_actor = Actor.objects.annotate(movie_count=Count("starring_actors")).order_by("-movie_count",
                                                                                      "full_name").first()

    top_actor_starring_movies = ", ".join([m.title for m in top_actor.starring_actors.all()])
    average_rating = sum([m.rating for m in top_actor.starring_actors.all()]) / len(
        [m.rating for m in top_actor.starring_actors.all()]) if [m.rating for m in
                                                                 top_actor.starring_actors.all()] else 0
    return f"Top Actor: {top_actor.full_name}, starring in movies: {top_actor_starring_movies}, movies average rating: {average_rating:.1f}"


def get_actors_by_movies_count():
    top_three_actors = Actor.objects.annotate(count_of_movies=Count("actor")).order_by(
        "-count_of_movies", "full_name")[:3]

    if not Movie.objects.all() or not top_three_actors:
        return ""

    result = []
    for actor in top_three_actors:
        result.append(f"{actor.full_name}, participated in {actor.count_of_movies} movies")

    return "\n".join(result)


def get_top_rated_awarded_movie():
    if not Movie.objects.filter(is_awarded=True):
        return ""

    highest_rated_movie = Movie.objects.filter(is_awarded=True).order_by("-rating", "title").first()

    highest_rated_movie_starring_actor = highest_rated_movie.starring_actor.full_name \
        if highest_rated_movie.starring_actor is not None\
        else "N/A"

    movie_actors = ", ".join([a.full_name for a in highest_rated_movie.actors.order_by("full_name")])

    return f"Top rated awarded movie: {highest_rated_movie.title}, rating: {highest_rated_movie.rating:.1f}. Starring actor: {highest_rated_movie_starring_actor}. Cast: {movie_actors}."


def increase_rating():
    classic_movies = Movie.objects.filter(is_classic=True, rating__lt=10)

    if not classic_movies:
        return "No ratings increased."

    for m in classic_movies:
        m.rating += Decimal(0.1)
        m.save()

    return f"Rating increased for {len(classic_movies)} movies."
