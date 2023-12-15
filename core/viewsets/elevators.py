from typing import Any

from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from core.models import Elevator, ElevatorRequest
from core.serializers import ElevatorRequestSerializer, ElevatorSerializer


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

    @action(
        methods=["get"],
        detail=True,
        name="requests",
        serializer_class=ElevatorRequestSerializer,
    )
    def requests(self, request, *args, **kwargs):
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
