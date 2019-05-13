from django_microservice_propaganda.propaganda import Propaganda, logger

from lms_events_handlers.lms_templates_data import get_new_enrollment_data, NEW_ENROLLMENT_SENDGRID_TEMPLATE_ID
from salalem_notifications.models import EmailNotificationData
from salalem_notifications_email_extension.tasks import AvailableEmailServiceProviders, send_email

propaganda = Propaganda("events")


def log_mq_exception(exception):
    logger.error('Exception occurred when handling MQ message: {0}'.format(exception))


def on_new_enrollment_handler(body, message):
    notification_data = EmailNotificationData.from_json(body['enrollment'])
    template_data = get_new_enrollment_data(notification_data)
    send_email(AvailableEmailServiceProviders.sendgrid, to_emails=[notification_data.to],
               template_id=NEW_ENROLLMENT_SENDGRID_TEMPLATE_ID,
               template_data=template_data,
               categories=[
                   "lms",
                   "enrollment",
                   "new"
               ])


def on_enrollment_valid_until_extended_handler(body, message):
    notification_data = EmailNotificationData.from_json(body['enrollment'])
    template_data = get_new_enrollment_data(notification_data)
    send_email(AvailableEmailServiceProviders.sendgrid, to_emails=[notification_data.to],
               template_id=NEW_ENROLLMENT_SENDGRID_TEMPLATE_ID,
               template_data=template_data,
               categories=[
                   "lms",
                   "enrollment",
                   "valid_until"
                   "extended"
               ])


def on_enrollment_allowed_attempts_changed_handler(body, message):
    notification_data = EmailNotificationData.from_json(body['enrollment'])
    template_data = get_new_enrollment_data(notification_data)
    send_email(AvailableEmailServiceProviders.sendgrid, to_emails=[notification_data.to],
               template_id=NEW_ENROLLMENT_SENDGRID_TEMPLATE_ID,
               template_data=template_data,
               categories=[
                   "lms",
                   "enrollment",
                   "valid_until"
                   "extended"
               ])


def on_enrollment_updated_status_failed_handler(body, message):
    notification_data = EmailNotificationData.from_json(body['enrollment'])
    template_data = get_new_enrollment_data(notification_data)
    send_email(AvailableEmailServiceProviders.sendgrid, to_emails=[notification_data.to],
               template_id=NEW_ENROLLMENT_SENDGRID_TEMPLATE_ID,
               template_data=template_data,
               categories=[
                   "lms",
                   "enrollment",
                   "graded",
                   "status",
                   "updated",
                   "failed"
               ])


def on_enrollment_updated_status_resubmit_handler(body, message):
    notification_data = EmailNotificationData.from_json(body['enrollment'])
    template_data = get_new_enrollment_data(notification_data)
    send_email(AvailableEmailServiceProviders.sendgrid, to_emails=[notification_data.to],
               template_id=NEW_ENROLLMENT_SENDGRID_TEMPLATE_ID,
               template_data=template_data,
               categories=[
                   "lms",
                   "enrollment",
                   "graded",
                   "status",
                   "updated",
                   "failed"
               ])


def on_certificate_ready_handler(body, message):
    notification_data = EmailNotificationData.from_json(body['certificate'])
    template_data = get_new_enrollment_data(notification_data)
    send_email(AvailableEmailServiceProviders.sendgrid, to_emails=[notification_data.to],
               template_id=NEW_ENROLLMENT_SENDGRID_TEMPLATE_ID,
               template_data=template_data,
               categories=[
                   "lms",
                   "enrollment",
                   "graded",
                   "status",
                   "updated",
                   "failed"
               ])


logger.error('Subscribing now')
print("--------")

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
    .on('lms.enrollment.certificate.status.ready', on_certificate_ready_handler,
        on_exception=log_mq_exception)
