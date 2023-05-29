import unittest
from json import JSONDecodeError

import requests

__unittest = True


class TestEndpoint(unittest.TestCase):

    url = "http://localhost:8080/currencies/usage"

    @classmethod
    def setUp(cls):
        x = None

    def test_json_array_length(self):
        try:
            res = requests.get(self.url)
        except Exception:
            self.fail('The /currencies/usage endpoint is not responding with a 200 status code. The application is not running or is having startup errors, check the logs.')
            return

        self.assertEqual(res.status_code, 200,
            "The /currencies/usage endpoint is not responding with a 200 status code.")

        try:
            res_dict = res.json()
            self.assertEqual(len(res_dict), 162,
                             "The response JSON should be an array. It was not of the expected length")
        except JSONDecodeError:
            self.fail("The response from the /currencies/usage endpoint could not be decoded as JSON")

if __name__ == "__main__":
    unittest.main()