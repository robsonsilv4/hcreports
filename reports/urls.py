from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import Index, ReportViewSet

router = DefaultRouter()
router.register("reports", ReportViewSet, basename="report")


urlpatterns = [
    path("", Index.as_view(), name="index"),
] + router.urls
