from django.core.management.base import BaseCommand

from api.db_test_data import workers, locations
from api.models.location import Location
from api.models.worker import Worker


class Command(BaseCommand):
    help = 'Add data to DB'

    def handle(self, *args, **options):
        for location in locations:
            Location.objects.get_or_create(
                nameLocation=location)



        for worker in workers:
            Worker.objects.get_or_create(
                full_name=worker,
            )








