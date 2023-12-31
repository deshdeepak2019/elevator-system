from rest_framework import serializers

from .models import Elevator, ElevatorRequest, ElevatorSystem


class ElevatorSystemSerializer(serializers.ModelSerializer):  # type: ignore[type-arg]
    class Meta:
        model = ElevatorSystem
        fields = ["id", "name", "max_floor", "number_of_elevators"]


class ElevatorSerializer(serializers.ModelSerializer):  # type: ignore[type-arg]
    class Meta:
        model = Elevator
        fields = "__all__"


class ElevatorRequestSerializer(serializers.ModelSerializer):  # type: ignore[type-arg]
    class Meta:
        model = ElevatorRequest
        fields = "__all__"


class FetchDestinationSerializer(serializers.Serializer):
    running = serializers.BooleanField()
    details = serializers.CharField()
    destination_floor = serializers.IntegerField(required=False, allow_null=True)
    current_floor = serializers.IntegerField(required=False, allow_null=True)
