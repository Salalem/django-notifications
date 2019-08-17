import os

from django.contrib import admin
from django.urls import path

if os.environ.get("BUILD_PROFILE", "") == "development":
    import lms_events_handlers.handlers

urlpatterns = [
    path("admin/", admin.site.urls),
]
