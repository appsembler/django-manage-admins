from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "list active staff"

    def handle(self, *args, **options):
        pass
