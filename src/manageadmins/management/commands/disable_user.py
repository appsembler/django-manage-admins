from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "disable user"

    def handle(self, *args, **options):
        self.stdout.write("disabling user")
