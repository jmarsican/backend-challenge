import json
from http import HTTPStatus
from typing import Any

from django.http import HttpRequest, HttpResponse
from pydantic import BaseModel, validator

from .models import Currency


class CountryDto(BaseModel):
    iso3: str
    common_name: str


class CurrencyUsageDto(BaseModel):
    code: str
    name: str
    countries: list[CountryDto]
    usages: int = 0

    @validator("usages", always=True)
    def calculate_usages(cls, v: int, values: dict[str, Any]) -> int:
        # usages is set to the length of the number of countries
        return len(values["countries"])


def usage(request: HttpRequest) -> HttpResponse:
    # Filter query results by single currency code if it exists
    # as a query string parameter
    code_query_param = request.GET.get("code")
    if code_query_param:
        return handle_currency_code_present(code_query_param)

    return get_all_currency_usages()


def handle_currency_code_present(code: str) -> HttpResponse:
    if len(code) != 3:
        # Return 400 Bad Request status code
        return HttpResponse(status=HTTPStatus.BAD_REQUEST)

    try:
        currency = Currency.objects.get(code=code)
    except Currency.DoesNotExist:
        # Return 404 Not Found status code
        return HttpResponse(status=HTTPStatus.NOT_FOUND)

    dto = build_currency_usage_dto_from_db_currency(currency)

    return HttpResponse(json.dumps([dto.dict()]))


def get_all_currency_usages() -> HttpResponse:
    currencies = Currency.objects.all()

    dtos = [
        build_currency_usage_dto_from_db_currency(currency) for currency in currencies
    ]

    dtos.sort(key=lambda currency_usage: (-currency_usage.usages, currency_usage.code))

    return HttpResponse(json.dumps([dto.dict() for dto in dtos]))


def build_currency_usage_dto_from_db_currency(currency: Currency) -> CurrencyUsageDto:
    return CurrencyUsageDto(
        code=currency.code,
        name=currency.name,
        countries=[
            CountryDto(iso3=country.cca3, common_name=country.common_name)
            for country in currency.country_set.all()
        ],
    )
