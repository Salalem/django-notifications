# -*- coding: utf-8 -*-
from advanced_filters.admin import AdminAdvancedFiltersMixin
from django.contrib import admin
from django.db.models import Q

from .models import Notification


def approve_notification(modeladmin, request, queryset):
    queryset.update(status='approved')


def send_notification(modeladmin, request, queryset):
    queryset = queryset.filter(Q(status="approved") | Q(status="error"))
    for notification in queryset.all():
        notification.send()


approve_notification.short_description = "Approve notifications (Send after)"
send_notification.short_description = "Send approved notifications"


class NotificationAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    list_per_page = 250
    list_display = ("status", "subject", "recipient_email", "created", "modified")
    list_filter = ("status", "subject", "recipient_email", "created", "modified")
    actions = [approve_notification, send_notification]

    advanced_filter_fields = (
        'recipient_email',
    )


admin.site.register(Notification, NotificationAdmin)
