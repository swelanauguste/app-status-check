from django.contrib import admin

from .models import Application


@admin.register(Application)
class ApplicationInline(admin.ModelAdmin):
    list_display = (
        "application_number",
        "nic_number",
        "receipt_number",
        "status",
        "email",
        'get_email_updates',
        "tel",
        "tel1",
        "details",
    )
