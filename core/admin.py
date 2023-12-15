from django.contrib import admin

from .models import Elevator, ElevatorSystem


@admin.register(Elevator)
class ElevatorAdmin(admin.ModelAdmin):
    model = Elevator


@admin.register(ElevatorSystem)
class ElevatorSystemAdmin(admin.ModelAdmin):
    model = ElevatorSystem
