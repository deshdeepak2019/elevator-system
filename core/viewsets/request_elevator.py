from rest_framework import mixins, viewsets

from core.models import ElevatorRequest
from core.serializers import ElevatorRequestSerializer


class ElevatorRequestViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = ElevatorRequest.objects.all()
    serializer_class = ElevatorRequestSerializer
    http_method_names = ["head", "get", "post", "patch"]
