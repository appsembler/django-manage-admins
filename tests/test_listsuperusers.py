from io import StringIO

from django.core.management import call_command
from django.test import TestCase

from .factories import UserFactory


class TestListSuperusers(TestCase):
    def call_command(self, *args, **kwargs):
        out = StringIO()
        call_command(
            "list_superusers",
            *args,
            stdout=out,
            stderr=StringIO(),
            **kwargs,
        )
        return out.getvalue()

    def test_command_exists(self):
        """just make sure the command even exists"""
        out = self.call_command()
        self.assertNotEqual(out, "")

    def test_includes_superuser(self):
        u = UserFactory(is_superuser=True)
        out = self.call_command()
        self.assertTrue(u.username in out)
