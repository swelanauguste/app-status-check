from django.core.mail import send_mail
from django.db import models
from django.utils.text import slugify

PRINTED = "PT"
ISSUED = "IS"
UNVERIFIED = "UV"
PROCESSING = "PS"

APP_STATUS_CHOICES = (
    (PRINTED, "Printed"),
    (ISSUED, "Issued"),
    (UNVERIFIED, "Unverified"),
    (PROCESSING, "Processing"),
)


class Application(models.Model):
    application_number = models.CharField(max_length=50, unique=True)
    nic_number = models.CharField("NIC number", max_length=50, unique=True)
    receipt_number = models.CharField(max_length=50, unique=True)
    status = models.CharField(
        max_length=2, choices=APP_STATUS_CHOICES, default=PROCESSING
    )
    slug = models.SlugField(max_length=50, blank=True, unique=True, null=True)
    details = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    get_email_updates = models.BooleanField(default=False)
    tel = models.CharField(
        "phone", max_length=25, blank=True, help_text="1-758-456-8500"
    )
    tel1 = models.CharField(
        "alt", max_length=25, blank=True, help_text="1-758-456-8501"
    )

    def save(self, *args, **kwargs):
        # Check if the model is being created or updated
        is_new = self.pk is None
        if not self.slug:
            self.slug = slugify(self.application_number)

        # Save the model
        super().save(*args, **kwargs)

        if is_new or self.get_email_updates:
            subject = "Department of Immigration"
            message = f"Your Application status is {self.get_status_display()} \n\n{self.details}"
            from_email = "no_eply@immigration.govt.lc.com"
            recipient_list = [self.email]

            send_mail(subject, message, from_email, recipient_list)

    def __str__(self):
        return self.status
