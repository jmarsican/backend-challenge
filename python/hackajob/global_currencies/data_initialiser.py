from .client.countries_client import CountriesClient
from .models import Country, Currency


class DataInitialiser(object):
    def __init__(self, countries_client: CountriesClient) -> None:
        self.countries_client = countries_client

    def initialise(self) -> None:
        # Don't initialize if we've already loaded everything
        if 250 == Country.objects.count():
            return

        self.storeInitialData()

    def storeInitialData(self) -> None:
        self.get_and_store_country_data()

        print("Data Initialiser executed")

    def get_and_store_country_data(self) -> None:
        countries = self.countries_client.get_countries()

        currency_map = {}
        countries_to_save = []
        country_currencies = []

        for country_dto in countries:
            print(f"Adding new Client Country: {country_dto.name.common}")
            c = Country(
                cca3=country_dto.iso3,
                common_name=country_dto.name.common,
                official_name=country_dto.name.official,
            )

            for code, currency_dto in country_dto.currencies.items():
                currency = currency_map.get(code)
                if currency is None:
                    print(f"  -> Adding new Client Currency: {code}")
                    currency = Currency(code=code, name=currency_dto.name)

                # Add Country & Currency Model pairing to list
                country_currencies.append((c, currency))
                currency_map[code] = currency

            countries_to_save.append(c)

        Country.objects.bulk_create(countries_to_save)
        Currency.objects.bulk_create(currency_map.values())

        # Bulk create the many-to-many relationships
        # Access the through model directly
        ThroughModel = Country.currencies.through
        ThroughModel.objects.bulk_create(
            [
                ThroughModel(country_id=country.id, currency_id=currency.id)
                for country, currency in country_currencies
            ]
        )
