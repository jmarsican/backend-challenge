from django.db import models


class Currency(models.Model):
    class Meta:
        db_table = "currency"

    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)


class Country(models.Model):
    class Meta:
        db_table = "country"
        ordering = ["cca3"]  # sort by country code asc by default

    cca3 = models.CharField(max_length=3)
    common_name = models.CharField(max_length=255)
    official_name = models.CharField(max_length=255)
    currencies = models.ManyToManyField(Currency, through="CountryCurrency")


class CountryCurrency(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["currency_id", "country_id"],
                name="currency_country_composite_unique_constraint",
            ),
        ]
        db_table = "country_currency"

    country = models.ForeignKey(Country, primary_key=True, on_delete=models.DO_NOTHING)
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING)
