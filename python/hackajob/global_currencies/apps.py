from django.apps import AppConfig


class GlobalCurrenciesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "global_currencies"

    def ready(self) -> None:
        # Code runs once on application start-up
        from .client.countries_client import CountriesClient
        from .data_initialiser import DataInitialiser

        countries_client = CountriesClient()
        DataInitialiser(countries_client=countries_client).initialise()

        return super().ready()
