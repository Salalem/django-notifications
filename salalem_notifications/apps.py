# -*- coding: utf-8 -*-
import os
import sys

from django.apps import AppConfig

from salalem_notifications.settings.base import IS_NOTIFICATION_SERVICE


class Config(AppConfig):
    name = "salalem_notifications"

    def ready(self):
        super(Config, self).ready()
        if IS_NOTIFICATION_SERVICE:
            if os.environ.get("BUILD_PROFILE", "") != "development":
                import lms_events_handlers.handlers

            import salalem_notifications.signals

            salalem_notifications.notify = salalem_notifications.signals.notify
