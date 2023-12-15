from core import viewsets

routes = {
    "v1": [
        (r"elevator-system", viewsets.ElevatorSystemViewSet, "system"),
        (r"elevator", viewsets.ElevatorViewSet, "system"),
        (r"elevator-request", viewsets.ElevatorRequestViewSet, "request"),
    ],
}
