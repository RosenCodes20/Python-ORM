import os
from datetime import date, timedelta

import django
from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()
from main_app.models import Author, Book, Artist, Song, Product, Review, Owner, Registration, Car, DrivingLicense


def show_all_authors_with_their_books():
    authors = Author.objects.all().order_by("id")
    result = []
    for author in authors:
        author_books = author.book_set.all()

        if not author_books:
            continue

        result.append(f"{author.name} has written - {', '.join(b.title for b in author_books)}!")

    return "\n".join(result)


def delete_all_authors_without_books():
    Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str) -> QuerySet:
    artist = Artist.objects.get(name=artist_name)

    return artist.songs.all().order_by("-id")


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    song.artists.remove(artist)


def calculate_licenses_expiration_dates():
    result = []
    all_licenses = DrivingLicense.objects.all().order_by("-license_number")

    for l in all_licenses:
        expiration_date = l.issue_date + timedelta(days=365)
        result.append(
            f"License with number: {l.license_number} expires on {expiration_date}!"
        )

    return "\n".join(result)


def get_drivers_with_expired_licenses(due_date: date):
    licenses = DrivingLicense.objects.all()
    expired_drivers = []
    for l in licenses:
        expiration_date = l.issue_date + timedelta(days=365)
        if expiration_date > due_date:
            expired_drivers.append(l.driver)

    return expired_drivers


def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.get(name=product_name)
    reviews = [r.rating for r in product.reviews.all()]

    average_rating_for_products = sum(reviews) / len(reviews)

    return average_rating_for_products


def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by("-name")


def delete_products_without_reviews():
    get_products_with_no_reviews().delete()


def register_car_by_owner(owner: Owner):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()

    car.owner = owner
    car.registration = registration
    car.save()

    registration.registration_date = date.today()

    registration.save()

    return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."



