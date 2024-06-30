import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Author, Book, Review


def find_books_by_genre_and_language(book_genre, book_language):
    return Book.objects.filter(genre=book_genre, language=book_language)


def find_authors_nationalities():
    authors_with_nationalities = Author.objects.exclude(nationality=None)
    result = []
    for author in authors_with_nationalities:
        result.append(f"{author.first_name} {author.last_name} is {author.nationality}")

    return "\n".join(map(str, result))


def order_books_by_year():
    ordered_books = Book.objects.all().order_by("publication_year", "title")
    result = []
    for book in ordered_books:
        result.append(f"{book.publication_year} year: {book.title} by {book.author}")

    return "\n".join(map(str, result))


def delete_review_by_id(review_id):
    review_with_id = Review.objects.get(id=review_id)
    review_with_id.delete()
    return f"Review by {review_with_id.reviewer_name} was deleted"


def filter_authors_by_nationalities(nationality):
    filtered_authors = Author.objects.filter(nationality=nationality).order_by("first_name", "last_name")
    result = []
    for author in filtered_authors:
        if author.biography is None:
            result.append(f"{author.first_name} {author.last_name}")

        else:
            result.append(author.biography)

    return "\n".join(map(str, result))


def filter_authors_by_birth_year(start_year, end_year):
    filtered_authors = Author.objects.filter(birth_date__year__range=(start_year, end_year)).order_by("-birth_date")
    result = []
    for author in filtered_authors:
        result.append(f"{author.birth_date}: {author.first_name} {author.last_name}")

    return "\n".join(map(str, result))


def change_reviewer_name(reviewer_name, new_name):
    updated_names = Review.objects.filter(reviewer_name=reviewer_name).update(reviewer_name=new_name)
    return Review.objects.all()

