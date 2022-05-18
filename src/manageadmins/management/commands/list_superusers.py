from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "list active superusers"

    def handle(self, *args, **options):
        self.stdout.write("running list_superusers")
