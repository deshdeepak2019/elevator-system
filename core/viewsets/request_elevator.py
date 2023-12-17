from typing import Any

from rest_framework import mixins, status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from core.models import ElevatorRequest, ElevatorSystem
from core.serializers import ElevatorRequestSerializer


class ElevatorRequestViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """API view set for ElevatorRequest model."""

    queryset = ElevatorRequest.objects.all()
    serializer_class = ElevatorRequestSerializer

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = ElevatorRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        system=ElevatorSystem.objects.get(elevator=serializer.validated_data["elevator"])
        
        if (
            serializer.validated_data["requested_floor"]
            == serializer.validated_data["destination_floor"]
        ):
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "details": "Requested floor and destination floor cannot be same"
                },
            )
        
        if (
            serializer.validated_data["requested_floor"]
            > system.max_floor
        ):
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "details": "Requested floor cannot be greater than max floor in elevator system"
                },
            )
        
        if (
            serializer.validated_data["destination_floor"]
            > system.max_floor
        ):
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "details": "Destination floor cannot be greater than max floor in elevator system"
                },
            )

        return super().create(request, *args, **kwargs)
