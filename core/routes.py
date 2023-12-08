from core import viewsets

routes = {
    "v1": [
        (r"elevator-system", viewsets.ElevatorSystemViewSet, "system"),
    ],
}