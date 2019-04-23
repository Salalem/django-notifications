from modeltranslation.translator import translator, TranslationOptions

from salalem_notifications.models import Notification


class NotificationTranslationOptions(TranslationOptions):
    fields = ("verb", "description")


translator.register(Notification, NotificationTranslationOptions)
