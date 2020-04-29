from django.shortcuts import render, get_object_or_404
from .models import playerModel


def index(request):
    players = playerModel.objects.order_by('-player_stat')
    top_players_five = []
    top_players_rest = []
    for i in range(5):
        temp_player = players[i]
        top_players_five.append(temp_player)
    for i in range(5,10):
        top_players_rest.append(players[i])
    context = {
        'players_five': top_players_five,
        'players_rest': top_players_rest,
    }
    return render(request,'crud/index.html',context)


def detail(request, player_pk):
    player = playerModel.objects.get(pk=player_pk)
    print(player)
    context = {
        'player': player,
    }
    return render(request, 'crud/detail.html', context)


def player_list(request):
    players = playerModel.objects.order_by('player_name')
    context = {
        'players': players,
        }
    return render(request, 'crud/player_list.html', context)

