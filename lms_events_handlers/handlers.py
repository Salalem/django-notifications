from django_microservice_propaganda.propaganda import Propaganda, logger
from pytz import unicode

from lms_events_handlers.lms_templates_data import get_new_enrollment_data, NEW_ENROLLMENT_SENDGRID_TEMPLATE_ID
from salalem_notifications_email_extension.tasks import AvailableEmailServiceProviders, send_email

propaganda = Propaganda("events")


def log_mq_exception(exception):
    logger.error('Exception occurred when handling MQ message: {0}'.format(exception))


def on_new_enrollment_handler(body, message):
    print("Message ---------->")
    print(message)
    print("Body ---------->")
    print({k: unicode(v).encode("utf-8") for k, v in body.items()})
    print("Data ---------->")
    print(body['enrollment']['user']['id'])
    template_data = get_new_enrollment_data(course_display_name=body['enrollment']['course']['title'],
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


propaganda.subscribe("lms.enrollment.#")\
    .on('lms.enrollment.new', on_new_enrollment_handler, on_exception=log_mq_exception)

