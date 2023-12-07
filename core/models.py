from django.db import models


class ElevatorSystem(models.Model):
  system_name = models.CharField(max_length = 32)
  max_floor = models.IntegerField()
  number_of_elevators = models.PositiveIntegerField()
