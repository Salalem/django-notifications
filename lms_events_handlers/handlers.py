from django_microservice_propaganda.propaganda import Propaganda, logger
from pytz import unicode

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
    print("-------")
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


logger.error('Subscribing now')
print("--------")

propaganda.subscribe("lms.enrollment.#")\
    .on('lms.enrollment.new', on_new_enrollment_handler, on_exception=log_mq_exception)\
    .on('lms.enrollment.updated.valid_until.extended', on_enrollment_valid_until_extended_handler, on_exception=log_mq_exception)\
    .on('lms.enrollment.updated.allowed_attempts.changed', on_enrollment_allowed_attempts_changed_handler, on_exception=log_mq_exception)

