from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

    def ready(self):
        """
        Running the another thread containing infinite loop
        """
        from .thread import RunThread

        RunThread().start()
