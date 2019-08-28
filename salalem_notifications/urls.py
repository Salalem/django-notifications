import os

from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

if os.environ.get("BUILD_PROFILE", "") == "development":
    import lms_events_handlers.handlers

urlpatterns = [
    path("admin/", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)