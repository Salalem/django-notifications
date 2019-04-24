# -*- coding: utf-8 -*-
from django.apps import AppConfig


class Config(AppConfig):
    name = "salalem_notifications"

    def ready(self):
        super(Config, self).ready()
        import salalem_notifications.signals
        import lms_events_handlers.handlers

        salalem_notifications.notify = salalem_notifications.signals.notify
