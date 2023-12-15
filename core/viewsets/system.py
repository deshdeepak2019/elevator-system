from typing import Any

from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from core.models import Elevator, ElevatorSystem
from core.serializers import ElevatorSerializer, ElevatorSystemSerializer


class ElevatorSystemViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer
    http_method_names = ["head", "get", "post", "patch"]

    @action(
        methods=["get"],
        detail=True,
        name="elevators",
        serializer_class=ElevatorSerializer,
    )
    def elevators(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        try:
            elevator = ElevatorSystem.objects.get(pk=kwargs["pk"])
        except ElevatorSystem.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        queryset = Elevator.objects.filter(elevator_system=elevator)
        page = self.paginate_queryset(queryset=queryset)
        serializer = ElevatorSerializer(
            page,
            many=True,
            context={"request": request},
        )
        paginated_response = self.get_paginated_response(serializer.data)
        return Response(paginated_response.data)
