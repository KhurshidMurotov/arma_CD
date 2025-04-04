from django.apps import AppConfig


class AboutConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.about"

    def ready(self) -> None:
        import apps.about.signals
