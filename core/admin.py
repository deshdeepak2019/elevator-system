from django.contrib import admin

from .models import Elevator, ElevatorRequest, ElevatorSystem


@admin.register(Elevator)
class ElevatorAdmin(admin.ModelAdmin):
    model = Elevator
    can_delete = False
    can_change = False
    list_display = (
        "id",
        "elevator_system",
        "current_floor",
        "is_operational",
        "is_door_open",
        "running_status",
    )


@admin.register(ElevatorSystem)
class ElevatorSystemAdmin(admin.ModelAdmin):
    model = ElevatorSystem
    can_delete = False
    can_change = False
    list_display = ("id", "name", "max_floor", "number_of_elevators")


@admin.register(ElevatorRequest)
class ElevatorSystemAdmin(admin.ModelAdmin):
    model = ElevatorRequest
