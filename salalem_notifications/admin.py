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


approve_notification.short_description = "Approve and send notifications"
send_notification.short_description = "Send notifications"


class NotificationAdmin(admin.ModelAdmin):
    list_display = ("status", )
    list_filter = ("status", "created", "modified")
    actions = [approve_notification, send_notification]


admin.site.register(Notification, NotificationAdmin)
