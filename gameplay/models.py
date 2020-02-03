from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
# Create your models here.

STATUS_CHOICES = [
    ("f", "First players to move"), 
    ("s", "Second players to move"),
    ("w", "First player won the game"), 
    ("l", "Second player won the game"), 
    ("d", "The was drawn")
]

class GamesQuerySet(models.QuerySet):
    def games_for_user(self, user):
        return self.filter(Q(first_player = user) | Q(second_player = user))

    def active(self):
        return self.filter(Q(status = 'f') | Q(status = 's'))


@python_2_unicode_compatible
class Game(models.Model):
    first_player = models.ForeignKey(User, related_name = "first_player_of_game", on_delete = models.CASCADE)
    second_player = models.ForeignKey(User, related_name = "second_player_of_game", on_delete = models.CASCADE)
    start_time = models.DateTimeField(auto_now_add = True)
    last_activity = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 1, choices = STATUS_CHOICES, default = 'f')
    objects = GamesQuerySet.as_manager()

    def __str__(self):
        return "{0} vs {1}".format(self.first_player, self.second_player)

class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length = 300, blank = True)
    by_first_player = models.BooleanField()
    game = models.ForeignKey(Game, on_delete = models.CASCADE)
