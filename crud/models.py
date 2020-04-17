from django.db import models

# Create your models here.


class playerModel(models.Model):
    player_name = models.CharField(max_length=30)
    team_name = models.CharField(max_length=30)
    player_stat = models.IntegerField()


