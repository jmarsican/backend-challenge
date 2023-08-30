from pydantic import BaseModel, Field


class CurrencyDto(BaseModel):
    name: str
    symbol: str


class NameDto(BaseModel):
    common: str
    official: str


class CountryDto(BaseModel):
    name: NameDto
    iso3: str = Field(alias="cca3")
    currencies: dict[str, CurrencyDto]
