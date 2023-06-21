import random

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import (
    APP_STATUS_CHOICES,
    ISSUED,
    PRINTED,
    PROCESSING,
    UNVERIFIED,
    Application,
)


class Command(BaseCommand):
    help = "Generates fake data using the Faker library."

    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(50):
            unique_6_digit_number = random.randint(100000, 999999)
            unique_10_digit_number = random.randint(1000000000, 9999999999)
            unique_12_digit_number = random.randint(100000000000, 999999999999)
            random_integer = random.randint(1, 4)

            def get_random_status():
                if random_integer == 1:
                    return PRINTED
                elif random_integer == 2:
                    return ISSUED
                elif random_integer == 3:
                    return UNVERIFIED
                elif random_integer == 4:
                    return PROCESSING

            yes_no = random.randint(0, 1)
            unique_email = fake.email()
            unique_telephone_number = fake.phone_number()
            details = fake.paragraph(nb_sentences=5)
            status = get_random_status()

            application = Application(
                application_number=unique_10_digit_number,
                nic_number=unique_6_digit_number,
                receipt_number=unique_12_digit_number,
                email=unique_email,
                get_email_updates=yes_no,
                status=status,
                tel=unique_telephone_number,
                tel1=unique_telephone_number,
                details=details,
            )
            application.save()
            # print(APP_STATUS_CHOICES[1])
            self.stdout.write(
                f"{unique_6_digit_number}, {get_random_status()}, {unique_10_digit_number},{unique_12_digit_number}, {random_integer},{unique_email}, {unique_telephone_number},{yes_no}, {details}"
            )
