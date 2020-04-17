from bs4 import BeautifulSoup as bs
import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BuildYourTeam.settings")
# 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()
from crud.models import playerModel

def baseModel():

    response = requests.get('https://www.ea.com/games/fifa/fifa-20/ratings/fifa-20-player-ratings-top-100')
    objects = response.text
    myFiFa = bs(objects,'lxml')

    names = []
    stats = []
    teams = []
    player_status = []

    #선수 이름
    players = bs.select(myFiFa,'ea-tile')

    for player in players:
        player = str(player)
        for i in range(len(player)-3):
            if player[i]+player[i+1]+player[i+2]+player[i+3] == '<h3>':
                stack = ''
                j = i+4
                while j < len(player):
                    if player[j] == '<':
                        break

                    stack += player[j]
                    j += 1
                if stack != '\n':
                    names.append(stack)

    #선수 스탯,
    cnt = 0
    cnt_a = 0
    for player in players:
        player = str(player)
        for i in range(len(player)-3):
            if player[i]+player[i+1]+player[i+2] == '<p>' and (player[i+3].isdigit() or player[i+4].isdigit()):
                #cnt_a += 1
                if player[i+3].isdigit():
                    stats.append(player[i+3]+player[i+4])

                elif player[i+4].isdigit():
                    stats.append(player[i+4]+player[i+5])

            elif player[i]+player[i+1]+player[i+2] == '<p>' and (player[i+3].isalpha() or player[i+4].isalpha()):

                j = 0

                if player[i+3].isalpha():
                    j = i+3
                elif player[i+4].isalpha():
                    j = i+4

                while j < len(player):
                    if player[j] == '<' or player[j] == '\xa0':
                        temp_team = player[i+3:j]
                        if temp_team != " ":
                            teams.append(temp_team.strip())
                        break
                    else:
                        j += 1

    for i in range(0,len(names)):
        player_status.append([names[i]])


    for i in range(len(teams)):
        teams[i] = teams[i].strip()
        if teams[i].strip() == "Piemonte Calcio":
            teams[i] = "Juventus"

        player_status[i].append(teams[i])

    for i in range(len(stats)):
        player_status[i].append(stats[i])

    return player_status


players_data = baseModel()


if __name__=='__main__':
    for player in players_data:
        db_player = playerModel()
        db_player.player_name = player[0]
        db_player.team_name = player[1]
        db_player.player_stat = player[2]
        db_player.save()