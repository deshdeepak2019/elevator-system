from typing import Any

from rest_framework import mixins, viewsets

from core.models import Elevator
from core.serializers import ElevatorSerializer
from rest_framework.request import Request
from rest_framework.response import Response


class ElevatorViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer
    http_method_names=["head","get","post","put"]
