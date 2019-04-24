# -*- coding: utf-8 -*-
import sys

from django.apps import AppConfig


class Config(AppConfig):
    name = "salalem_notifications"

    def ready(self):
        super(Config, self).ready()
        if 'runserver' not in sys.argv:
            return True

        import salalem_notifications.signals

        salalem_notifications.notify = salalem_notifications.signals.notify
