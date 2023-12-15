from django.views.generic import TemplateView
from django.urls import include, path
from rest_framework.routers import DefaultRouter


from .routes import routes
from rest_framework.schemas import get_schema_view
from core import viewsets


router = DefaultRouter()

urlpatterns = [
    path(
        "openapi/",
        get_schema_view(
            title="Elevator System API",
            description="All API's for Elevator system",
            version="1.0.0",
        ),
        name="openapi-schema",
    ),
    path(
        "",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
]

router.register("elevator-system", viewsets.ElevatorSystemViewSet, basename="elevator-system")
router.register("elevator", viewsets.ElevatorViewSet, basename="elevator")



urlpatterns += [
    path("", include(router.urls)),
]