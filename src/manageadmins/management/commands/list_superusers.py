from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "list active superusers"

    def handle(self, *args, **options):
        User = get_user_model()
        superusers = User.objects.filter()
        self.stdout.write("\n".join([s.username for s in superusers]))
