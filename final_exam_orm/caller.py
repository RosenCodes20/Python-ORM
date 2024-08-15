import os
import django
from django.db.models import Q, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

#    tar.exe -a -cf project.zip main_app orm_skeleton caller.py manage.py requirements.txt

from main_app.models import Astronaut, Spacecraft, Mission


def get_astronauts(search_string=None):

    if not Astronaut.objects.all() or search_string is None:
        return ""

    astronauts = Astronaut.objects.filter(Q(name__icontains=search_string)
                                            |
                                         Q(phone_number__icontains=search_string)).order_by("name")

    if not astronauts:
        return ""

    result = []

    for astronaut in astronauts:
        result.append(f"Astronaut: {astronaut.name}, phone number: {astronaut.phone_number}, status: {'Active' if astronaut.is_active else 'Inactive'}")

    return "\n".join(result)


def get_top_astronaut():

    if not Astronaut.objects.all() or not Mission.objects.all():
        return "No data."

    top_astronaut = Astronaut.objects.annotate(count_of_missions=Count("astronauts")).order_by("-count_of_missions", "phone_number").first()

    if not top_astronaut:
        return "No data."

    return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.count_of_missions} missions."


def get_top_commander():

    if not Astronaut.objects.all() or not Mission.objects.all() or not Mission.objects.filter(commander_id__gt=0):
        return "No data."

    top_commander = Astronaut.objects.annotate(count_of_commaned_missions=Count("commander")).order_by("-count_of_commaned_missions", "phone_number").first()
    if not top_commander:
        return "No data."

    return f"Top Commander: {top_commander.name} with {top_commander.count_of_commaned_missions} commanded missions."


def get_last_completed_mission():

    if not Mission.objects.filter(status__exact="Completed"):
        return "No data."

    last_completed_mission = Mission.objects.filter(status__exact="Completed").order_by("launch_date").last()

    astronauts = ", ".join([a.name for a in last_completed_mission.astronauts.all().order_by("name")])

    spacewalks = sum([a.spacewalks for a in last_completed_mission.astronauts.all()])

    return f"The last completed mission is: {last_completed_mission.name}. Commander: {last_completed_mission.commander.name if last_completed_mission.commander else 'TBA'}. Astronauts: {astronauts}. Spacecraft: {last_completed_mission.spacecraft.name}. Total spacewalks: {spacewalks}."


def get_most_used_spacecraft():

    if not Mission.objects.all():
        return "No data."

    most_used_spacecraft = Spacecraft.objects.annotate(count_of_missions=Count("mission")).order_by("-count_of_missions", "name").first()
    astronaut_length = 0
    astronauts_in_mission = [m.astronauts.all().distinct() for m in most_used_spacecraft.mission_set.all()]
    astronauts_ids = []
    for astronaut in astronauts_in_mission:
        for astronauts in astronaut:
            if astronauts.id not in astronauts_ids:
                astronauts_ids.append(astronauts.id)

    astronaut_length += len(astronauts_ids)

    return f"The most used spacecraft is: {most_used_spacecraft.name}, manufactured by {most_used_spacecraft.manufacturer}, used in {most_used_spacecraft.count_of_missions} missions, astronauts on missions: {astronaut_length}."


def decrease_spacecrafts_weight():

    spacecrafts = Spacecraft.objects.filter(mission__status="Planned", weight__gte=200).distinct()

    if not spacecrafts:
        return "No changes in weight."

    for spacecraft in spacecrafts:
        spacecraft.weight -= 200
        spacecraft.save()

    avg_weight_after_decrease = Spacecraft.objects.aggregate(avg_weight=Avg("weight"))

    return (f"The weight of {len(spacecrafts)} spacecrafts has been decreased. The new average weight of all "
            f"spacecrafts is {avg_weight_after_decrease['avg_weight'] or 0:.1f}kg")
