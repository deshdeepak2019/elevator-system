from typing import Any

from rest_framework import mixins, viewsets,status

from core.models import Elevator
from core.serializers import ElevatorSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from drf_spectacular.utils import OpenApiParameter, extend_schema


class ElevatorViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer
    http_method_names=["head","get","post","patch"]

    def get_queryset(self):
        return super().get_queryset()
    
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="system_id",
                type=int,
                required=True,
            )
        ],
        responses={
            status.HTTP_200_OK: ElevatorSerializer,
        },
    )
    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return Response(status=200)
