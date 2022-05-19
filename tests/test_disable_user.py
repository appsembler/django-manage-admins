from io import StringIO

from django.core.management import call_command
from django.test import TestCase


class TestDisableUser(TestCase):
    def call_command(self, *args, **kwargs):
        out = StringIO()
        call_command(
            "disable_user",
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
