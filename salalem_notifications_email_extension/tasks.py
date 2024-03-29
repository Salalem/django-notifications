from django.core.mail import EmailMessage


class AvailableEmailServiceProviders:
    sendgrid = "sendgrid"


def send_email(provider, from_email="Salalem <training-center@salalem.com>",
               to_emails=None,
               reply_to_email_header="training@salalem.com",
               attachment=None,
               **kwargs):

    if to_emails is None:
        to_emails = []
    if not provider:
        raise Exception("A provider arg should be specified")

    if not isinstance(to_emails, list):
        raise Exception("to_emails arg should be a list of email addresses")

    if len(to_emails) == 0:
        raise Exception("to_emails list should have at-least one email address")

    mail = EmailMessage(
        from_email=from_email,
        to=to_emails,
        headers={"Reply-To": reply_to_email_header},
    )
    mail.content_subtype = "html"
    if provider == AvailableEmailServiceProviders.sendgrid:
        if "template_id" not in kwargs:
            raise Exception("A template_id arg should be specified with provider: " + provider)

        mail.template_id = kwargs.get("template_id")
        if "template_data" not in kwargs:
            raise Exception("A template_data arg should be specified with provider: " + provider)
        dynamic_data =  kwargs.get("template_data")
        try:
            if dynamic_data["c2a_link"].startswith("https://salalem.com"):
	            dynamic_data["c2a_link"] = dynamic_data["c2a_link"].replace("https://salalem.com", "https://demo.salalem.com")
        except:
            pass
                
        mail.dynamic_template_data = kwargs.get("template_data")

        if "categories" not in kwargs:
            raise Exception("A categories list should be specified with provider: " + provider)

        mail.categories = kwargs.get("categories")

    # # Attach file
    # with open('somefilename.pdf', 'rb') as file:
    #     mail.attachments = [
    #         ('somefilename.pdf', file.read(), 'application/pdf')
    #     ]

    if attachment:
        mail.attach('Enrollments Report.xlsx', attachment,
                     'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    # Add categories
    return mail.send(fail_silently=False)
