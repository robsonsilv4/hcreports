from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("", include("reports.urls")),
    path("users/", include("users.urls")),
    path("admin/", admin.site.urls),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT,
)
