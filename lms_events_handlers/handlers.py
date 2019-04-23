from django_microservice_propaganda.propaganda import Propaganda, logger
from pytz import unicode

propaganda = Propaganda("events")


def log_mq_exception(exception):
    logger.error('Exception occurred when handling MQ message: {0}'.format(exception))


def on_new_enrollment_handler(body, message):
    print({k: unicode(v).encode("utf-8") for k, v in body.items()})
    print({k: unicode(v).encode("utf-8") for k, v in message.items()})


propaganda.subscribe("lms.enrollment.#")\
    .on('lms.enrollment.new', on_new_enrollment_handler, on_exception=log_mq_exception)
