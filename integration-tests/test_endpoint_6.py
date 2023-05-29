import unittest
from json import JSONDecodeError

import requests

__unittest = True


class TestEndpoint(unittest.TestCase):

    url = "http://localhost:8080/currencies/usage?code=GBP"

    @classmethod
    def setUp(cls):
        x = None

    def test_valid_currency_code_query_parameter(self):
        try:
            res = requests.get(self.url)
        except Exception:
            self.fail('The /currencies/usage?code=GBP endpoint is not responding with a 200 status code. '
                      'The application is not running or is having startup errors, check the logs.')
            return

        self.assertEqual(res.status_code, 200,
                         "The /currencies/usage endpoint is not responding with a 200 status code.")

        try:
            res_dict = res.json()
        except JSONDecodeError:
            self.fail("The response from the /currencies/usage endpoint could not be decoded as JSON")

        expected_dict = {
           "GBP": ["GGY", "SHN", "JEY", "GBR", "IMN"]
        }

        actual_dict = {}
        self.assertEqual(len(res_dict), 1, "The response array should be of length one when a currency code "
                                           "that is found in the database is provided in the query string.")
        for i in res_dict:
            self.assertEqual(i["usages"], 5, "Unexpected value for usages when currency code is GBP")
            self.assertEqual(i["code"], "GBP", "Unexpected value for code when currency code is GBP")
            self.assertEqual(i["name"], "British pound", "Unexpected value for name when currency code is GBP")
            country_codes = []
            for c in i['countries']:
                country_codes.append(c['iso3'])
            actual_dict[i['code']] = country_codes

        for (k, v), (k2, v2) in zip(actual_dict.items(), expected_dict.items()):
            self.assertEqual(k, k2,
                             "Unexpected currency code ordering")
            self.assertEqual(v, sorted(v2),
                             "Unexpected country ordering of the countries array")


if __name__ == "__main__":
    unittest.main()