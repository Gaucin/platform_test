from django.db import models

from events.models import Event


class Booking(models.Model):
    customer = models.ForeignKey("User", on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
