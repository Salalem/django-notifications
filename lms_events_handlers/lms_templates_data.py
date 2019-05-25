NEW_ENROLLMENT_SENDGRID_TEMPLATE_ID = "d-ae481a0937c645f094a83ea3937c5f2c"
ATTACHMENT_EMAIL_SENDGRID_TEMPLATE_ID = "d-bdb18aabfa3f41f59a84ddc873372535"


def _get_base_data():
    return {
        "facebook": True,
        "facebook_link": "https://facebook.com/salalemlearning",
        "twitter": True,
        "twitter_link": "https://twitter.com/salalemlearning",
        "youtube": True,
        "youtube_link": "https://www.youtube.com/channel/UCpdFdi06qC7Qbnmz0mNJkyQ",
        "linkedin": True,
        "linkedin_link": "https://www.linkedin.com/company/salalem",
        "instagram": True,
        "instagram_link": "https://www.instagram.com/salalemlearning"
    }

def get_new_enrollment_data(notification_data):
    full_data = {}
    full_data.update(_get_base_data())
    full_data.update({
        "subject": notification_data.subject,
        "header": notification_data.header.format(notification_data.extra_data["course_display_name"]),
        "text": notification_data.text.format(notification_data.extra_data["platform_name"],
                                              notification_data.extra_data["course_display_name"]),
        "secondary_text": notification_data.secondary_text.format(notification_data.extra_data["deadline"]),

        "signature": notification_data.signature,
        "c2a_link": notification_data.c2a_link,
        "c2a_button": notification_data.c2a_button,
        "footer_text": notification_data.footer_text
    })
    return full_data


def get_new_certificate_data(notification_data):
    full_data = {}
    full_data.update(_get_base_data())
    full_data.update({
        "subject": notification_data.subject,
        "header": notification_data.header.format(notification_data.extra_data["course_display_name"]),
        "text": notification_data.text.format(notification_data.extra_data["platform_name"],
                                              notification_data.extra_data["course_display_name"]),
        "secondary_text": "",
        "signature": notification_data.signature,
        "c2a_link": notification_data.c2a_link,
        "c2a_button": notification_data.c2a_button,
        "footer_text": notification_data.footer_text
    })
    return full_data


def get_new_enrollment_reporting_attachment_data(notification_data):
    full_data = {}
    full_data.update(_get_base_data())
    full_data.update({
        "subject": notification_data.subject,
        "header": notification_data.header,
        "text": notification_data.text,
        "footer_text": notification_data.footer_text
    })
    return full_data
