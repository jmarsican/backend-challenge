import unittest

import requests

__unittest = True


class TestEndpoint(unittest.TestCase):

    url = "http://192.168.0.86:8080/currencies/usage?code=XYZ"

    @classmethod
    def setUp(cls):
        x = None

    def test_invvalid_currency_code_query_parameter(self):
        try:
            res = requests.get(self.url)
        except Exception:
            self.fail('The /currencies/usage endpoint is not responding.'
                      'The application is not running or is having startup errors, check the logs.')

        self.assertEqual(res.status_code, 404,
                         "The /currencies/usage endpoint is not responding with a 404 NOT FOUND status code "
                         "if a currency code that is not in the database is supplied e.g. code=XYZ.")


if __name__ == "__main__":
    unittest.main()
