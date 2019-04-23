# -*- coding: utf-8 -*-
from django.apps import AppConfig

from lms_events_handlers.lms_templates_data import get_new_enrollment_data, NEW_ENROLLMENT_SENDGRID_TEMPLATE_ID
from salalem_notifications_email_extension.tasks import send_email, AvailableEmailServiceProviders


class Config(AppConfig):
    name = "salalem_notifications"

    def ready(self):
        super(Config, self).ready()
        import salalem_notifications.signals
        salalem_notifications.notify = salalem_notifications.signals.notify

        template_data = get_new_enrollment_data(course_display_name="Anti-Money Laundry",
                                enrollment_link="https://salalem.com",
                                signature="Salalem Team",
                                footer_text="For help, please contact us anytime using the live chat feature available on the website")

        send_email(AvailableEmailServiceProviders.sendgrid, to_emails=["firas@salalem.com"],
                   template_id=NEW_ENROLLMENT_SENDGRID_TEMPLATE_ID,
                   template_data=template_data,
                   categories=[
                       "lms",
                       "enrollment",
                       "new"
                   ])
