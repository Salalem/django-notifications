# -*- coding: utf-8 -*-
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


class NotificationAdmin(admin.ModelAdmin):
    list_display = ("recipient_email", "subject", "status")
    list_filter = ("recipient_email", "subject", "status", "created", "modified")
    actions = [approve_notification, send_notification]


admin.site.register(Notification, NotificationAdmin)
