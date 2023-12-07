from django.db import models

class RunningStatus(models.IntegerChoices):
    '''
    Choices for running status of the elevator system
    '''
    GOING_UP = 1
    STANDING_STILL = 0
    GOING_DOWN = -1

class ElevatorSystem(models.Model):
  """
  Represents a building with multiple elevators, utilizing Django's 
  default ID as the primary key; assumes a minimum floor of 0, with 
  easy implementation for dynamic minimum floor.
  """
  system_name = models.CharField(max_length = 32)
  max_floor = models.IntegerField()
  number_of_elevators = models.PositiveIntegerField()


class Elevator(models.Model):
  """
  A singular movable unit within an elevator system, inherently linked 
  as a foreign key to the overall system.
  """

  elevator_system = models.ForeignKey(ElevatorSystem , on_delete=models.CASCADE)

  elevator_number = models.IntegerField()
  current_floor = models.PositiveSmallIntegerField(default=0)

  is_operational = models.BooleanField(default=True)
  is_door_open = models.BooleanField(default=True)
  running_status = models.IntegerField(choices=RunningStatus.choices,default=0)