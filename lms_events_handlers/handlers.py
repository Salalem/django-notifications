import json
from io import BytesIO

from django_microservice_propaganda.propaganda import Propaganda, logger

from lms_events_handlers.lms_templates_data import get_new_enrollment_data, CALL_TO_ACTION_SENDGRID_TEMPLATE_ID, \
    get_new_certificate_data, ATTACHMENT_EMAIL_SENDGRID_TEMPLATE_ID, get_new_enrollment_reporting_attachment_data, \
    get_account_activation_data
from salalem_notifications.models import EmailNotificationData, Notification
from salalem_notifications_email_extension.tasks import AvailableEmailServiceProviders, send_email

propaganda = Propaganda("events")


def log_mq_exception(exception):
    logger.error('Exception occurred when handling MQ message: {0}'.format(exception))


def on_new_enrollment_handler(body, message):
    notification_data = EmailNotificationData.from_json(body['enrollment'])
    Notification.new(recipient_email=notification_data.to, subject=notification_data.subject,
                     content=notification_data.text, template_type="enrollment",
                     extra_data=notification_data.extra_data,
                     full_data=str(notification_data.to_json()),
                     template_id=CALL_TO_ACTION_SENDGRID_TEMPLATE_ID,
                     categories=json.dumps([
                         "lms",
                         "enrollment",
                         "new"
                     ]))


def on_enrollment_valid_until_extended_handler(body, message):
    print(body)
    notification_data = EmailNotificationData.from_json(body['enrollment'])
    Notification.new(recipient_email=notification_data.to, subject=notification_data.subject,
                     content=notification_data.text, template_type="enrollment",
                     extra_data=notification_data.extra_data,
                     full_data=str(notification_data.to_json()),
                     template_id=CALL_TO_ACTION_SENDGRID_TEMPLATE_ID,
                     categories=json.dumps([
                         "lms",
                         "enrollment",
                         "valid_until"
                         "extended"
                     ]))


def on_enrollment_allowed_attempts_changed_handler(body, message):
    notification_data = EmailNotificationData.from_json(body['enrollment'])
    Notification.new(recipient_email=notification_data.to, subject=notification_data.subject,
                     content=notification_data.text, template_type="enrollment",
                     extra_data=notification_data.extra_data,
                     full_data=str(notification_data.to_json()),
                     template_id=CALL_TO_ACTION_SENDGRID_TEMPLATE_ID,
                     categories=json.dumps([
                         "lms",
                         "enrollment",
                         "valid_until"
                         "extended"
                     ]))


def on_enrollment_updated_status_failed_handler(body, message):
    notification_data = EmailNotificationData.from_json(body['enrollment'])
    Notification.new(recipient_email=notification_data.to, subject=notification_data.subject,
                     content=notification_data.text, template_type="enrollment",
                     extra_data=notification_data.extra_data,
                     full_data=str(notification_data.to_json()),
                     template_id=CALL_TO_ACTION_SENDGRID_TEMPLATE_ID,
                     categories=json.dumps([
                         "lms",
                         "enrollment",
                         "graded",
                         "status",
                         "updated",
                         "failed"
                     ]))


def on_enrollment_updated_status_resubmit_handler(body, message):
    notification_data = EmailNotificationData.from_json(body['enrollment'])
    Notification.new(recipient_email=notification_data.to, subject=notification_data.subject,
                     content=notification_data.text, template_type="enrollment",
                     extra_data=notification_data.extra_data,
                     full_data=str(notification_data.to_json()),
                     template_id=CALL_TO_ACTION_SENDGRID_TEMPLATE_ID,
                     categories=json.dumps([
                         "lms",
                         "enrollment",
                         "graded",
                         "status",
                         "updated",
                         "failed"
                     ]))


def on_certificate_ready_handler(body, message):
    print(body)
    notification_data = EmailNotificationData.from_json(body['certificate'])
    Notification.new(recipient_email=notification_data.to, subject=notification_data.subject,
                     content=notification_data.text, template_type="certificate",
                     extra_data=notification_data.extra_data,
                     full_data=str(notification_data.to_json()),
                     template_id=CALL_TO_ACTION_SENDGRID_TEMPLATE_ID,
                     categories=json.dumps([
                         "lms",
                         "certificate",
                         "issue",
                     ]
                     ))


def on_enrollment_dealine_approaching_handler(body, message):
    notification_data = EmailNotificationData.from_json(body['enrollment'])
    Notification.new(recipient_email=notification_data.to, subject=notification_data.subject,
                     content=notification_data.text, template_type="enrollment",
                     extra_data=notification_data.extra_data,
                     full_data=str(notification_data.to_json()),
                     template_id=CALL_TO_ACTION_SENDGRID_TEMPLATE_ID,
                     categories=json.dumps([
                         "lms",
                         "enrollment",
                         "deadline",
                         "approaching",
                         "user"
                     ]))


def on_enrollment_reporting_new_xls(body, message):
    notification_data = EmailNotificationData.from_json(body['report'])
    template_data = get_new_enrollment_reporting_attachment_data(notification_data)
    send_email(AvailableEmailServiceProviders.sendgrid, to_emails=[notification_data.to],
               template_id=ATTACHMENT_EMAIL_SENDGRID_TEMPLATE_ID,
               template_data=template_data,
               categories=[
                   "lms",
                   "enrollment_reporting",
                   "xls",
                   "new"
               ],
               attachment=bytes.fromhex(notification_data.extra_data['xls_data']))


def on_enrollment_updated_status_overdue_handler(body, message):
    notification_data = EmailNotificationData.from_json(body['enrollment'])
    Notification.new(recipient_email=notification_data.to, subject=notification_data.subject,
                     content=notification_data.text, template_type="enrollment",
                     extra_data=notification_data.extra_data,
                     full_data=str(notification_data.to_json()),
                     template_id=CALL_TO_ACTION_SENDGRID_TEMPLATE_ID,
                     categories=json.dumps([
                         "lms",
                         "enrollment",
                         "graded",
                         "status",
                         "updated",
                         "overdue"
                     ]))


def on_account_activation_email(body, message):
    notification_data = EmailNotificationData.from_json(body['data'])
    Notification.new(recipient_email=notification_data.to, subject=notification_data.subject,
                     content=notification_data.text, template_type="account",
                     extra_data=notification_data.extra_data,
                     full_data=str(notification_data.to_json()),
                     template_id=CALL_TO_ACTION_SENDGRID_TEMPLATE_ID,
                     categories=json.dumps([
                         "lms",
                         "account",
                         "activation",
                     ]))


logger.error('Subscribing now')
logger.error('Subscribing to lms.enrollment.#')

propaganda.subscribe("lms.enrollment.#") \
    .on('lms.enrollment.new', on_new_enrollment_handler, on_exception=log_mq_exception) \
    .on('lms.enrollment.updated.valid_until.extended', on_enrollment_valid_until_extended_handler,
        on_exception=log_mq_exception) \
    .on('lms.enrollment.updated.allowed_attempts.changed', on_enrollment_allowed_attempts_changed_handler,
        on_exception=log_mq_exception) \
    .on('lms.enrollment.updated.status.failed', on_enrollment_updated_status_failed_handler,
        on_exception=log_mq_exception) \
    .on('lms.enrollment.updated.status.resubmit', on_enrollment_updated_status_resubmit_handler,
        on_exception=log_mq_exception) \
    .on('lms.enrollment.deadline.approaching', on_enrollment_dealine_approaching_handler,
        on_exception=log_mq_exception) \
    .on('lms.enrollment.updated.status.overdue', on_enrollment_updated_status_overdue_handler,
        on_exception=log_mq_exception)

logger.error('Subscribing to lms.certificate.#')

propaganda.subscribe("lms.certificate.#") \
    .on('lms.certificate.status.ready', on_certificate_ready_handler,
        on_exception=log_mq_exception)

logger.error('Subscribing to lms.enrollment_reporting.#')
propaganda.subscribe("lms.enrollment_reporting.#") \
    .on('lms.enrollment_reporting.new.xls', on_enrollment_reporting_new_xls, on_exception=log_mq_exception)

logger.error('Subscribing to lms.account.#')
propaganda.subscribe("lms.account.#") \
    .on('lms.account.activation', on_account_activation_email,
        on_exception=log_mq_exception)
