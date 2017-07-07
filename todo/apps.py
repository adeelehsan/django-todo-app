from __future__ import unicode_literals

from django.apps import AppConfig


class TodoConfig(AppConfig):
    name = 'todo'

    def ready(self):
        from signals.signals import update_log