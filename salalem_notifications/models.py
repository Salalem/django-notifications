# -*- coding: utf-8 -*-
# pylint: disable=too-many-lines
import json

from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_noop
from model_utils.models import TimeStampedModel


class EmailNotificationData(object):
    def __init__(self, to=None, cc=None,
                 subject=None, header=None,
                 text=None, secondary_text=None,
                 signature=None, c2a_link=None,
                 c2a_button=None, footer_text=None,
                 extra_data=None):
        self.to = to
        self.cc = cc
        self.subject = subject
        self.header = header
        self.text = text
        self.secondary_text = secondary_text
        self.signature = signature
        self.c2a_link = c2a_link
        self.c2a_button = c2a_button
        self.footer_text = footer_text
        self.extra_data = extra_data

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

    def to_json(self):
        return json.dumps(self.__dict__)


EXTRA_DATA = True

NOTIFICATION_STATUSES = (
    ("in_review", gettext_noop("In Review")),
    ("approved", gettext_noop("Approved")),
    ("sent", gettext_noop("Sent")),
    ("delivered", gettext_noop("Delivered")),
    ("error", gettext_noop("Error")),
)


class Notification(TimeStampedModel):
    recipient_email = models.TextField()
    subject = models.TextField()
    content = models.TextField()
    template_type = models.TextField()
    extra_data = models.TextField(null=True, blank=True, default={})
    full_data = models.TextField()
    template_id = models.TextField()
    categories = models.TextField()
    error = models.TextField(null=True, blank=True)
    status = models.CharField(
        blank=True,
        null=True,
        max_length=16,
        db_index=True,
        choices=NOTIFICATION_STATUSES,
    )

    def send(self):
        from salalem_notifications_email_extension.tasks import send_email, AvailableEmailServiceProviders
        from lms_events_handlers.lms_templates_data import get_new_enrollment_data, get_new_certificate_data, \
            get_account_activation_data, get_new_enrollment_reporting_attachment_data
        if self.status == "approved" or self.status == "error":
            template_data = None
            if self.template_type == "enrollment":
                template_data = get_new_enrollment_data(EmailNotificationData.from_json(self.full_data))
            elif self.template_type == "certificate":
                template_data = get_new_certificate_data(EmailNotificationData.from_json(self.full_data))
            elif self.template_type == "account":
                template_data = get_account_activation_data(EmailNotificationData.from_json(self.full_data))
            elif self.template_type == "reporting":
                template_data = get_new_enrollment_reporting_attachment_data(
                    EmailNotificationData.from_json(self.full_data))
            else:
                raise Exception("Notification does not define a type")

            print(template_data)
            print(json.loads(self.categories))

            try:
                print(json.loads(self.categories))
                result = send_email(AvailableEmailServiceProviders.sendgrid, to_emails=[self.recipient_email],
                                    template_id=self.template_id,
                                    template_data=template_data,
                                    categories=[json.loads(self.categories)])
                self.status = "delivered"
                if self.error:
                    self.error = None
            except Exception as error:
                self.status = "error"
                self.error = error
            self.save()
        else:
            raise Exception("Notification is already sent or delivered")

    @classmethod
    def new(cls, recipient_email, subject, content, template_type, extra_data, full_data, template_id, categories):
        notification, created = cls.objects.get_or_create(recipient_email=recipient_email, subject=subject,
                                                          content=content, template_type=template_type,
                                                          extra_data=extra_data, status="in_review",
                                                          template_id=template_id,
                                                          full_data=full_data, categories=json.dumps(categories))
        notification.save()
        return notification
