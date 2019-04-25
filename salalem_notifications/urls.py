import os

if os.environ.get("BUILD_PROFILE", "") == "development":
    import lms_events_handlers.handlers

urlpatterns = []
