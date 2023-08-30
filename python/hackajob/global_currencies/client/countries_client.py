import requests
from pydantic import parse_obj_as

from .models import CountryDto


class CountriesClient(object):
    URL = "https://s3.eu-west-1.amazonaws.com/hackajob-assets1.p.hackajob/challenges/global_currency_usage/index.json"

    def __init__(self) -> None:
        self.client = requests.Session()

    def get_countries(self) -> list[CountryDto]:
        response = self.client.get(self.URL)
        return parse_obj_as(list[CountryDto], response.json())
