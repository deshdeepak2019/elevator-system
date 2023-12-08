from typing import Any

from rest_framework import mixins, viewsets

from core.models import ElevatorSystem
from core.serializers import ElevatorSystemSerializer
from rest_framework.request import Request
from rest_framework.response import Response


class ElevatorSystemViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,  # Add other mixins if needed
    viewsets.GenericViewSet,
):
    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer
