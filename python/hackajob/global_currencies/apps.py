from django.apps import AppConfig


class GlobalCurrenciesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "global_currencies"

    def ready(self) -> None:
        # Code runs once on application start-up
        from .data_initialiser import DataInitialiser

        DataInitialiser().initialise()

        return super().ready()
