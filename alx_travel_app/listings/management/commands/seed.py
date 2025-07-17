from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random

fake = Faker()


class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding listings...")

        for _ in range(10):
            Listing.objects.create(
                title=fake.catch_phrase(),
                description=fake.paragraph(nb_sentences=5),
                price_per_night=round(random.uniform(50, 500), 2),
                location=fake.city()
            )

        self.stdout.write(self.style.SUCCESS("✅ Successfully seeded listings"))
