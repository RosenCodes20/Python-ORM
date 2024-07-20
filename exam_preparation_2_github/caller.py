import os
import django
from django.db.models import Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import TennisPlayer, Tournament, Match


# from dummy import populate_model_with_data
# tar.exe -a -cf project.zip main_app orm_skeleton caller.py manage.py requirements.txt

def get_tennis_players(search_name=None, search_country=None):
    result = []
    if search_name is not None and search_country is not None:
        tennis_players = TennisPlayer.objects.filter(
            full_name__contains=search_name,
            country__contains=search_country
        ).order_by("ranking")

    elif search_name is not None and search_country is None:
        tennis_players = TennisPlayer.objects.filter(
            full_name__contains=search_name
        ).order_by("ranking")

    elif search_name is None and search_country is not None:
        tennis_players = TennisPlayer.objects.filter(
            country__contains=search_country
        ).order_by("ranking")

    else:
        return ""

    for player in tennis_players:
        result.append(f"Tennis Player: {player.full_name}, country: {player.country}, ranking: {player.ranking}")

    return "\n".join(result)


def get_top_tennis_player():
    top_tennis_player = TennisPlayer.objects.annotate(wins=Count("winners")).order_by("-wins", "full_name").first()

    if not TennisPlayer.objects.all():
        return ""

    return f"Top Tennis Player: {top_tennis_player.full_name} with {top_tennis_player.wins} wins."


def get_tennis_player_by_matches_count():
    if not Match.objects.all() or not TennisPlayer.objects.all():
        return ""

    most_played_tennis_player = TennisPlayer.objects.annotate(most_games=Count("players_played")).order_by("-most_games", "ranking").first()

    return f"Tennis Player: {most_played_tennis_player.full_name} with {most_played_tennis_player.most_games} matches played."


def get_tournaments_by_surface_type(surface=None):
    if not Tournament.objects.all() or surface is None:
        return ""

    result = []
    filtered_tournaments = Tournament.objects.filter(
        surface_type__icontains=surface).annotate(num_matches=Count("tournaments")).order_by("-start_date")

    for tournament in filtered_tournaments:
        result.append(f"Tournament: {tournament.name}, start date: {tournament.start_date}, matches: {tournament.num_matches}")

    return "\n".join(result)


def get_latest_match_info():
    last_match = Match.objects.all().order_by("date_played", "id").last()

    if not Match.objects.all():
        return ""

    players_full_names = " vs ".join([p.full_name for p in last_match.players.all().order_by("full_name")])

    winner = last_match.winner.full_name if last_match.winner is not None else "TBA"

    return f"Latest match played on: {last_match.date_played}, tournament: {last_match.tournament.name}, score: {last_match.score}, players: {players_full_names}, winner: {winner}, summary: {last_match.summary}"


def get_matches_by_tournament(tournament_name=None):
    matches = Match.objects.filter(tournament__name__exact=tournament_name).order_by("-date_played")
    result = []
    if not matches or not Tournament.objects.all() or tournament_name is None or not Match.objects.all():
        return "No matches found."

    for match in matches:
        winner = match.winner.full_name if match.winner is not None else "TBA"
        result.append(f"Match played on: {match.date_played}, score: {match.score}, winner: {winner}")

    return "\n".join(result)


print(get_tournaments_by_surface_type("not selected"))