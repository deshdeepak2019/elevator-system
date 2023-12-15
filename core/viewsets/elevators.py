from typing import Any

from rest_framework import mixins, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from core.models import Elevator
from core.serializers import ElevatorSerializer


class ElevatorViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer
    http_method_names = ["head", "get", "post", "patch"]

    def get_queryset(self):
        return super().get_queryset()

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = ElevatorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return super().create(request, *args, **kwargs)
