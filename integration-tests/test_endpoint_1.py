import unittest
from json import JSONDecodeError

import requests

__unittest = True


class TestEndpoint(unittest.TestCase):

    url = "http://localhost:8080/currencies/usage"

    @classmethod
    def setUp(cls):
        x = None

    def test_endpoint(self):
        try:
            res = requests.get(self.url)
        except Exception:
            self.fail('The /currencies/usage endpoint is not responding with a 200 status code. The application is not running or is having startup errors, check the logs.')
            return

        self.assertEqual(res.status_code, 200,
            "The /currencies/usage endpoint is not responding with a 200 status code.")

if __name__ == "__main__":
    unittest.main()