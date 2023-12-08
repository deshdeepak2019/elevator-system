from .models import Elevator,ElevatorSystem
from rest_framework import serializers


class ElevatorSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorSystem
        fields = ["id","system_name","max_floor","number_of_elevators"]

class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = '__all__'