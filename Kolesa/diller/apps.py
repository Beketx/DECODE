from django.apps import AppConfig


class DillerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'diller'

    def ready(self):  # method just to import the signals
            import diller.signals