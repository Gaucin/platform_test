from random import choices
from django.db import models

from events.constants import EVENT_TYPES
from rooms.models import Room


class Event(models.Model):
    description = models.CharField(max_length=60)
    type = models.IntegerField(choices=EVENT_TYPES)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
