from django.shortcuts import render
from gameplay.models import Game
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()
    # games_first_player = Game.objects.filter(first_player = request.user, status = 'f')
    # games_second_player = Game.objects.filter(second_player = request.user, status = 's')
    # all_my_games = list(games_first_player)+ list(games_second_player)
    return render(request, "player/home.html",  
                        {"games": active_games })
