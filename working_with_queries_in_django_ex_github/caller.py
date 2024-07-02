import os
from typing import List

import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


#from dummy import populate_model_with_data
from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal, Dungeon, Workout
from main_app.choices import LaptopBrandChoices, OperationSystemChoice, MealChoices, DungeonDifficultyChoices, \
    WorkoutTypeChoices


def show_highest_rated_art():
    highest_rated_art = ArtworkGallery.objects.order_by("-rating", "id").first()

    return f"{highest_rated_art.art_name} is the highest-rated art with a {highest_rated_art.rating} rating!"


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery):
    ArtworkGallery.objects.bulk_create(
        [
            first_art,
            second_art
        ]
    )


def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop():
    highest_paid_laptop = Laptop.objects.order_by("-price", "-id").first()

    return f"{highest_paid_laptop.brand} is the most expensive laptop available for {highest_paid_laptop.price}$!"


def bulk_create_laptops(args: List[Laptop]):
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage():
    (Laptop.objects.filter(
        brand__in=(LaptopBrandChoices.ASUS, LaptopBrandChoices.LENOVO
                     )
    )
     .update(storage=512)
     )


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=(
        LaptopBrandChoices.ACER,
        LaptopBrandChoices.APPLE,
        LaptopBrandChoices.DELL
    )).update(memory=16)


def update_operation_systems():
    (Laptop.objects.filter(
        brand=LaptopBrandChoices.ASUS
    )
     .update(operation_system=OperationSystemChoice.WINDOWS))

    Laptop.objects.filter(
        brand=LaptopBrandChoices.APPLE
    ).update(operation_system=OperationSystemChoice.MAC_OS)

    Laptop.objects.filter(
        brand__in=(
            LaptopBrandChoices.DELL,
            LaptopBrandChoices.ACER
        )
    ).update(operation_system=OperationSystemChoice.LINUX)

    Laptop.objects.filter(
        brand=LaptopBrandChoices.LENOVO
    ).update(operation_system=OperationSystemChoice.CHROME_OS)


def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()


def bulk_create_chess_players(args: List[ChessPlayer]):
    ChessPlayer.objects.bulk_create(args)


def delete_chess_players():
    ChessPlayer.objects.filter(title="no title").delete()


def change_chess_games_won():
    ChessPlayer.objects.filter(title="GM").update(games_won=30)


def change_chess_games_lost():
    ChessPlayer.objects.filter(title="no title").update(games_lost=25)


def change_chess_games_drawn():
    ChessPlayer.objects.update(games_drawn=10)


def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title="GM")


def grand_chess_title_IM():
    ChessPlayer.objects.filter(rating__range=(2300, 2399)).update(title="IM")


def grand_chess_title_FM():
    ChessPlayer.objects.filter(rating__range=(2200, 2299)).update(title="FM")


def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__range=(0, 2199)).update(title="regular player")


def set_new_chefs():
    Meal.objects.filter(meal_type=MealChoices.BREAKFAST).update(chef="Gordon Ramsay")
    Meal.objects.filter(meal_type=MealChoices.LUNCH).update(chef="Julia Child")
    Meal.objects.filter(meal_type=MealChoices.DINNER).update(chef="Jamie Oliver")
    Meal.objects.filter(meal_type=MealChoices.SNACK).update(chef="Thomas Keller")


def set_new_preparation_times():
    Meal.objects.filter(meal_type=MealChoices.BREAKFAST).update(preparation_time="10 minutes")
    Meal.objects.filter(meal_type=MealChoices.LUNCH).update(preparation_time="12 minutes")
    Meal.objects.filter(meal_type=MealChoices.DINNER).update(preparation_time="15 minutes")
    Meal.objects.filter(meal_type=MealChoices.SNACK).update(preparation_time="5 minutes")


def update_low_calorie_meals():
    Meal.objects.filter(meal_type__in=(MealChoices.BREAKFAST, MealChoices.DINNER)).update(
        calories=400
    )


def update_high_calorie_meals():
    Meal.objects.filter(meal_type__in=(MealChoices.LUNCH, MealChoices.SNACK)).update(
        calories=700
    )


def delete_lunch_and_snack_meals():
    Meal.objects.filter(meal_type__in=(MealChoices.LUNCH, MealChoices.SNACK)).delete()


def show_hard_dungeons():
    hard_locations = Dungeon.objects.filter(difficulty="Hard").order_by("-location")
    result = []

    for location in hard_locations:
        result.append(f"{location.name} is guarded by {location.boss_name} who has {location.boss_health} health points!")

    return "\n".join(map(str, result))


def bulk_create_dungeons(args: List[Dungeon]):
    Dungeon.objects.bulk_create(args)


def update_dungeon_names():
    (Dungeon.objects.filter(difficulty=DungeonDifficultyChoices.EASY)
     .update(name="The Erased Thombs"))

    Dungeon.objects.filter(difficulty=DungeonDifficultyChoices.MEDIUM).update(
        name="The Coral Labyrinth"
    )

    Dungeon.objects.filter(difficulty=DungeonDifficultyChoices.HARD).update(
        name="The Lost Haunt"
    )


def update_dungeon_bosses_health():
    Dungeon.objects.exclude(difficulty=DungeonDifficultyChoices.EASY).update(boss_health=500)


def update_dungeon_recommended_levels():
    Dungeon.objects.filter(difficulty=DungeonDifficultyChoices.EASY).update(recommended_level=25)
    Dungeon.objects.filter(difficulty=DungeonDifficultyChoices.MEDIUM).update(recommended_level=50)
    Dungeon.objects.filter(difficulty=DungeonDifficultyChoices.HARD).update(recommended_level=75)


def update_dungeon_rewards():
    Dungeon.objects.filter(boss_health=500).update(reward="1000 Gold")
    Dungeon.objects.filter(location__startswith="E").update(reward="New dungeon unlocked")
    Dungeon.objects.filter(location__endswith="s").update(reward="Dragonheart Amulet")


def set_new_locations():
    Dungeon.objects.filter(recommended_level=25).update(location="Enchanted Maze")
    Dungeon.objects.filter(recommended_level=50).update(location="Grimstone Mines")
    Dungeon.objects.filter(recommended_level=75).update(location="Shadowed Abyss")


def show_workouts():
    filtered_workouts = Workout.objects.filter(
        workout_type__in=(
            WorkoutTypeChoices.CALISTHENICS,
            WorkoutTypeChoices.CROSSFIT
        )).order_by("id")

    result = []

    for workout in filtered_workouts:
        result.append(
            f"{workout.name} from {workout.workout_type} type has {workout.difficulty} difficulty!"
        )

    return "\n".join(map(str, result))


def get_high_difficulty_cardio_workouts():
    return Workout.objects.filter(workout_type="Cardio", difficulty="High").order_by("instructor")


def set_new_instructors():
    Workout.objects.filter(workout_type=WorkoutTypeChoices.CARDIO).update(instructor="John Smith")
    Workout.objects.filter(workout_type=WorkoutTypeChoices.STRENGTH).update(instructor="Michael Williams")
    Workout.objects.filter(workout_type=WorkoutTypeChoices.YOGA).update(instructor="Emily Johnson")
    Workout.objects.filter(workout_type=WorkoutTypeChoices.CROSSFIT).update(instructor="Sarah Davis")
    Workout.objects.filter(workout_type=WorkoutTypeChoices.CALISTHENICS).update(instructor="Chris Heria")


def set_new_duration_times():
    Workout.objects.filter(instructor="John Smith").update(duration="15 minutes")
    Workout.objects.filter(instructor="Sarah Davis").update(duration="30 minutes")
    Workout.objects.filter(instructor="Chris Heria").update(duration="45 minutes")
    Workout.objects.filter(instructor="Michael Williams").update(duration="1 hour")
    Workout.objects.filter(instructor="Emily Johnson").update(duration="1 hour and 30 minutes")


def delete_workouts():
    Workout.objects.exclude(workout_type__in=("Strength", "Calisthenics")).delete()
