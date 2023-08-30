## Running this reference solution

Built using Python 3.10.

If using the Poetry package manager, you can run the following to install dependencies

```bash
poetry install
```

Otherwise, there is also a `requirements.txt` that mirrors the `poetry.lock` file and can be installed via `pip`:

```bash
pip install -r requirements.txt
```

You can then start the Django server from within the `hackajob` directory with the following:

```bash
cd hackajob
poetry run python manage.py runserver 0.0.0.0:8080
```

## Backend application: global currency usage

Your task is to create a small backend application. Please read the instructions and run the tests as many times as you need in order to validate your solution.

You are provided with a public API endpoint that delivers JSON data about countries and the currencies that are used in that country.

You are required to store some of the data from the endpoint in a PostgreSQL database using the supplied schema. The schema is `hackajob_global_currencies` in the default `postgres` database.

You are then required to build an application that delivers JSON from a single endpoint with path `/currencies/usage` based on processing the data that was collected from the public API endpoint.

A `pyproject.toml` file is provided to enable construction of the application using `Django` (web framework), `requests` (HTTP client), `pydantic` (data modelling), and `psycopg` (database client). You have also been provided with some outline classes and code to structure your application and facilitate the build out.

A skeleton Django application is provided within the `hackajob` directory. This application also includes a `DataInitialiser` class. This class will execute and run before the main application starts within the `hackajob/global_currencies/apps.py` file. The expectation is that you will implement code in the DataInitialiser class to capture data from the public API endpoint and store some of it in the database.

**Note: the skeleton application was built using Python 3.10**

The application can be started by running `python manage.py runserver 0.0.0.0:8080` and handles requests to the `/currencies/usage` endpoint using the data stored in the database.

The public API endpoint is: <https://s3.eu-west-1.amazonaws.com/hackajob-assets1.p.hackajob/challenges/global_currency_usage/index.json>. It provides a list of country information including currency usage in the country and some additional data.

* The mapping of fields from the JSON data from the public API endpoints to the database tables should be self-evident. In general database field names closely match fields in the JSON data.
* Do not modify the provided data schema.
* Any data from the public API endpoint that does not fit into the database can be discarded.
* The schema is set up to capture only the data that you need to build out the required endpoint in your application.

Although the cca3 (or iso) three letter uppercase country code and the three letter uppercase currency code are unique identifiers, the database is set up to use a unique integer id as a primary key in each table (except the country_currency join table).

country_currency is a join or association table to support the many-to-many mapping between countries and currencies. A country can have multiple currencies and a currency can be used by multiple countries.

* The REST API endpoint in the Django application should be made available at `/currencies/usage`.
* The output data should be in JSON format and be an array of objects (sample snippet for two currency objects shown below) showing each currency (3 letter code and name), the number of countries that use the currency (usages) and a list of countries (the iso3 code and the commonName for the country) that use the currency e.g.

```json
[
  ...
  {
    "code": "SHP",
    "name": "Saint Helena pound",
    "countries": [
      {
        "iso3": "SGS",
        "commonName": "South Georgia"
      },
      {
        "iso3": "SHN",
        "commonName": "Saint Helena, Ascension and Tristan da Cunha"
      }
    ],
    "usages": 2
  },
  {
    "code": "AED",
    "name": "United Arab Emirates dirham",
    "countries": [
      {
        "iso3": "ARE",
        "commonName": "United Arab Emirates"
      }
    ],
    "usages": 1
  },
  ...
]
```

* The JSON output should be sorted in descending order of usages with the most used currency first.
* The currency code should be used to order currencies with the same number of usages.
* The list of countries using each currency should be an array sorted by iso3 country code.
* Even if the currency is used by only one country the countries field should still be an array containing only one object.
* Your endpoint should also support an optional query string parameter code which can have a value of a *single* three letter currency code.
* When the code parameter is present and a corresponding currency is found in the database, the JSON output should just be information for that single currency. The output should be an array containing a single currency object (as previously described).
* If the value of the code parameter when present is not a three letter string then the endpoint should return a 400 Bad Request status code.
* If the value of the code parameter is a three letter string but no matching currency is found in the database the endpoint should return a 404 Not Found status code.
