NEW_ENROLLMENT_SENDGRID_TEMPLATE_ID = "d-ae481a0937c645f094a83ea3937c5f2c"


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


def get_new_enrollment_data(course_display_name, enrollment_link, signature="", footer_text=""):
    full_data = {}
    full_data.update(_get_base_data())
    full_data.update({
                    "subject": "New Course Enrollment",
                    "header": "New Enrollment in " + course_display_name,
                    "text": "You have been enrolled in: " + course_display_name + ", you can go directly to the studying material by clicking the link below",
                    "signature": signature,
                    "c2a_link": enrollment_link,
                    "c2a_button": "Go to course",
                    "footer_text": footer_text
                })
    return full_data
