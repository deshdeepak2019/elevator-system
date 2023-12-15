from django.db import models


class RunningStatus(models.IntegerChoices):
    """
    Choices for running status of the elevator system
    """

    GOING_UP = 1
    STANDING_STILL = 0
    GOING_DOWN = -1


class CreatedModifiedBaseModel(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
        help_text="Datetime when this object was created",
    )
    modified_on = models.DateTimeField(
        auto_now=True,
        help_text="Datetime when this object was last modified",
    )

    class Meta:
        abstract = True


class ElevatorSystem(CreatedModifiedBaseModel):
    """
    Represents a building with multiple elevators, utilizing Django's
    default ID as the primary key; assumes a minimum floor of 0, with
    easy implementation for dynamic minimum floor.
    """

    system_name = models.CharField(max_length=32, help_text="Name of elevator system")
    max_floor = models.IntegerField(help_text="Maximum floor in a elevator system")
    number_of_elevators = models.PositiveIntegerField(
        help_text="Maximum number of elevators in a elevator system"
    )


class Elevator(CreatedModifiedBaseModel):
    """
    A singular movable unit within an elevator system, inherently linked
    as a foreign key to the overall system.
    """

    elevator_system = models.ForeignKey(
        ElevatorSystem,
        on_delete=models.CASCADE,
        help_text="ID of elevator system , from which system this elevator belongs to.",
    )
    current_floor = models.PositiveSmallIntegerField(
        default=0, help_text="Current floor"
    )
    is_operational = models.BooleanField(
        default=True, help_text="Whether the elevator is operational or not."
    )
    is_door_open = models.BooleanField(
        default=True, help_text="Whether the door is open or not."
    )
    running_status = models.IntegerField(
        choices=RunningStatus.choices,
        default=0,
        help_text="Running status of elevator means, UP,DOWN..",
    )


class ElevatorRequest(CreatedModifiedBaseModel):
    """
    Elevator Request by user.
    """

    elevator = models.ForeignKey(
        Elevator,
        on_delete=models.CASCADE,
        help_text="ID of elevator which is requested by user.",
    )
    requested_floor = models.PositiveSmallIntegerField(
        help_text="Requested floor by user."
    )
    destination_floor = models.PositiveSmallIntegerField(
        help_text="Destination floor at which user wants to go."
    )
    request_time = models.DateTimeField(
        auto_now_add=True, help_text="Time at which user requested for elevator."
    )
    is_active = models.BooleanField(default=True)
