import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom


#from dummy import populate_model_with_data

# Create queries within functions


def create_pet(name, species):
    Pet.objects.create(
        name=name,
        species=species
    )

    return f"{name} is a very cute {species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )

    return f"The artifact {name} is {age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    ordered_locations = Location.objects.all().order_by("-id")

    result = []

    for location in ordered_locations:
        result.append(f"{location.name} has a population of {location.population}!")

    return "\n".join(map(str, result))


def new_capital():
    first_location = Location.objects.first()

    first_location.is_capital = True

    first_location.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values("name")


def delete_first_location():
    Location.objects.first().delete()


def apply_discount():
    all_cars = Car.objects.all()
    for car in all_cars:
        sum_price_discount = sum(int(p) for p in str(car.year)) / 100

        car.price_with_discount = float(car.price) - float(car.price) * sum_price_discount

        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gt=2020).values("model", "price_with_discount")


def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks():
    tasks = Task.objects.all()
    result = []
    for task in tasks:
        result.append(f"Task - {task.title} needs to be done until {task.due_date}!")

    return "\n".join(map(str, result))


def complete_odd_tasks():
    tasks = Task.objects.all()

    for task in tasks:
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text, task_title):
    filtered_tasks = Task.objects.filter(title=task_title)

    for task in filtered_tasks:
        task.description = "".join(map(str, [chr(ord(letter) - 3) for letter in text]))
        task.save()


def get_deluxe_rooms():
    all_rooms = HotelRoom.objects.all()
    result = []
    for room in all_rooms:
        if room.room_type == "Deluxe" and room.id % 2 == 0:
            result.append(f"Deluxe room with number {room.room_number} costs {room.price_per_night}$ per night!")

    return "\n".join(map(str, result))


def increase_room_capacity():
    reserved_rooms = HotelRoom.objects.filter(is_reserved=True).order_by("id")
    previous_room = None
    for room in reserved_rooms:

        if previous_room is not None:
            room.capacity += previous_room

        else:
            room.capacity += room.id

        previous_room = room.capacity
        room.save()

def reserve_first_room():
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room():
    last_room = HotelRoom.objects.last()

    if not last_room.is_reserved:
        last_room.delete()


increase_room_capacity()
