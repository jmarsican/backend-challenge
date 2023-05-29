import unittest

import requests

__unittest = True


class TestEndpoint(unittest.TestCase):

    url = "http://localhost:8080/currencies/usage?code=invalid"

    @classmethod
    def setUp(cls):
        x = None

    def test_invvalid_currency_code_query_parameter(self):
        try:
            res = requests.get(self.url)
        except Exception:
            self.fail('The /currencies/usage endpoint is not responding.'
                      'The application is not running or is having startup errors, check the logs.')

        self.assertEqual(res.status_code, 400,
                         "The /currencies/usage endpoint is not responding with a 400 BAD REQUEST status code "
                         "if an invalid currency code parameter is supplied e.g. code=invalid "
                         "Valid currency codes are three characters long.")


if __name__ == "__main__":
    unittest.main()