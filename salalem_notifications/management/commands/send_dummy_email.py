# coding: utf-8
import json

from django.core.management import BaseCommand

# The class must be named Command, and subclass BaseCommand

from lms_events_handlers.lms_templates_data import CALL_TO_ACTION_SENDGRID_TEMPLATE_ID
from salalem_notifications.models import EmailNotificationData

from salalem_notifications_email_extension.tasks import send_email, AvailableEmailServiceProviders


class Command(BaseCommand):
    help = "Send dummy email"

    def handle(self, *args, **options):
        certificate_notification_data = EmailNotificationData()
        certificate_notification_data.to = "SAl-bahri@hbtf.com.jo"
        certificate_notification_data.subject = "Test email"
        certificate_notification_data.header = "Test {0} Email"
        certificate_notification_data.text = "Test email {1}"
        certificate_notification_data.secondary_text = ""
        certificate_notification_data.c2a_button = "Test"
        certificate_notification_data.c2a_link = "https://test"
        certificate_notification_data.signature = "مركز التدريب والتطوير"
        certificate_notification_data.extra_data = {
            'platform_name': "منصة تمكين للتعليم والتدريب الالكتروني",
            'course_display_name': "test"
        }
        certificate_notification_data.footer_text = "ننصحك بتحميل اخر تحديث لمتصفح الانترنت الذي تستخدمه. للمساعدة، يرجی التواصل مع فريق سلالم من خلال الايقونة الظاهرة في الزاوية السفلی من المنصة"

        send_email(AvailableEmailServiceProviders.sendgrid, to_emails=[certificate_notification_data.to],
                   template_id=CALL_TO_ACTION_SENDGRID_TEMPLATE_ID,
                   template_data=certificate_notification_data.__dict__,
                   categories=[
                       "lms",
                       "certificate",
                       "issue",
                   ])
