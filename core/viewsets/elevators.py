from typing import Any

from django.db.models.query import QuerySet
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from core.models import Elevator, ElevatorRequest
from core.serializers import (
    ElevatorRequestSerializer,
    ElevatorSerializer,
    FetchDestinationSerializer,
)


class ElevatorViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,  # type:ignore[type-arg]
):
    """API view set for Elevator model."""

    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer
    http_method_names = ["head", "get", "post", "patch"]

    def get_queryset(self) -> QuerySet[Elevator]:
        return super().get_queryset()

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = ElevatorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return super().create(request, *args, **kwargs)

    @action(
        methods=["get"],
        detail=True,
        name="requests",
        serializer_class=ElevatorRequestSerializer,
    )
    def requests(self, request: Request, *args: Any, **kwargs: Any):
        try:
            elevator = Elevator.objects.get(pk=kwargs["pk"])
        except Elevator.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        queryset = ElevatorRequest.objects.filter(elevator=elevator)
        page = self.paginate_queryset(queryset=queryset)
        serializer = ElevatorRequestSerializer(
            page,
            many=True,
            context={"request": request},
        )
        paginated_response = self.get_paginated_response(serializer.data)
        return Response(paginated_response.data)

    @action(
        methods=["get"],
        detail=True,
        name="fetch-destination",
        serializer_class=FetchDestinationSerializer,
    )
    def fetch_destination(
        self, request: Request, *args: Any, **kwargs: Any
    ) -> Response:
        data = {}
        try:
            elevator = Elevator.objects.get(pk=kwargs["pk"])
        except Elevator.DoesNotExist:
            data = {
                "running": False,
                "details": "Elevator doesn't exist",
                "current_floor": None,
                "destination_floor": None,
            }
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=data,
            )

        elevator_request = ElevatorRequest.objects.filter(elevator=elevator).order_by(
            "-request_time"
        )

        if not elevator.is_operational:
            data = {
                "running": False,
                "details": "The Elevator is not operational",
                "current_floor": elevator.current_floor,
                "destination_floor": None,
            }
        elif elevator_request.count() == 0:
            data = {
                "running": False,
                "details": "No pending requests",
                "current_floor": elevator.current_floor,
                "destination_floor": None,
            }
        else:
            data = {
                "running": True,
                "details": f"Final destination of last request for this elevator is {elevator_request[0].destination_floor}",
                "current_floor": elevator.current_floor,
                "destination_floor": elevator_request[0].destination_floor,
            }
        serializer = FetchDestinationSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return Response(status=status.HTTP_200_OK, data=serializer.data)
