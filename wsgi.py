"""
WSGI config for salalem_notifications project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.environ.get("BUILD_PROFILE", "") == "staging":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "salalem_notifications.settings.production")
elif os.environ.get("BUILD_PROFILE", "") == "production":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "salalem_notifications.settings.production")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "salalem_notifications.settings.development")

application = get_wsgi_application()
