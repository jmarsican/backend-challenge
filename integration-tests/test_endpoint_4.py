import unittest
from json import JSONDecodeError

import requests

__unittest = True


class TestEndpoint(unittest.TestCase):

    url = "http://192.168.0.86:8080/currencies/usage"

    @classmethod
    def setUp(cls):
        x = None

    def test_json_ordering_and_usages_values(self):
        try:
            res = requests.get(self.url)
        except Exception:
            self.fail('The /currencies/usage endpoint is not responding with a 200 status code. The application is not running or is having startup errors, check the logs.')
            return

        self.assertEqual(res.status_code, 200,
            "The /currencies/usage endpoint is not responding with a 200 status code.")

        try:
            res_dict = res.json()
        except JSONDecodeError:
            self.fail("The response from the /currencies/usage endpoint could not be decoded as JSON")

        expected_currency_usages_dict = {"EUR": 36, "USD": 20, "XCD": 8, "XOF": 8, "AUD": 7, "XAF": 6, "GBP": 5,
                                         "NZD": 5, "ZAR": 4, "DKK": 3, "XPF": 3, "ANG": 2, "CHF": 2, "DZD": 2, "EGP": 2,
                                         "ILS": 2, "INR": 2, "JOD": 2, "MAD": 2, "MRU": 2, "NOK": 2, "SGD": 2, "SHP": 2,
                                         "AED": 1, "AFN": 1, "ALL": 1, "AMD": 1, "AOA": 1, "ARS": 1, "AWG": 1, "AZN": 1,
                                         "BAM": 1, "BBD": 1, "BDT": 1, "BGN": 1, "BHD": 1, "BIF": 1, "BMD": 1, "BND": 1,
                                         "BOB": 1, "BRL": 1, "BSD": 1, "BTN": 1, "BWP": 1, "BYN": 1, "BZD": 1, "CAD": 1,
                                         "CDF": 1, "CKD": 1, "CLP": 1, "CNY": 1, "COP": 1, "CRC": 1, "CUC": 1, "CUP": 1,
                                         "CVE": 1, "CZK": 1, "DJF": 1, "DOP": 1, "ERN": 1, "ETB": 1, "FJD": 1, "FKP": 1,
                                         "FOK": 1, "GEL": 1, "GGP": 1, "GHS": 1, "GIP": 1, "GMD": 1, "GNF": 1, "GTQ": 1,
                                         "GYD": 1, "HKD": 1, "HNL": 1, "HTG": 1, "HUF": 1, "IDR": 1, "IMP": 1, "IQD": 1,
                                         "IRR": 1, "ISK": 1, "JEP": 1, "JMD": 1, "JPY": 1, "KES": 1, "KGS": 1, "KHR": 1,
                                         "KID": 1, "KMF": 1, "KPW": 1, "KRW": 1, "KWD": 1, "KYD": 1, "KZT": 1, "LAK": 1,
                                         "LBP": 1, "LKR": 1, "LRD": 1, "LSL": 1, "LYD": 1, "MDL": 1, "MGA": 1, "MKD": 1,
                                         "MMK": 1, "MNT": 1, "MOP": 1, "MUR": 1, "MVR": 1, "MWK": 1, "MXN": 1, "MYR": 1,
                                         "MZN": 1, "NAD": 1, "NGN": 1, "NIO": 1, "NPR": 1, "OMR": 1, "PAB": 1, "PEN": 1,
                                         "PGK": 1, "PHP": 1, "PKR": 1, "PLN": 1, "PYG": 1, "QAR": 1, "RON": 1, "RSD": 1,
                                         "RUB": 1, "RWF": 1, "SAR": 1, "SBD": 1, "SCR": 1, "SDG": 1, "SEK": 1, "SLL": 1,
                                         "SOS": 1, "SRD": 1, "SSP": 1, "STN": 1, "SYP": 1, "SZL": 1, "THB": 1, "TJS": 1,
                                         "TMT": 1, "TND": 1, "TOP": 1, "TRY": 1, "TTD": 1, "TVD": 1, "TWD": 1, "TZS": 1,
                                         "UAH": 1, "UGX": 1, "UYU": 1, "UZS": 1, "VES": 1, "VND": 1, "VUV": 1, "WST": 1,
                                         "YER": 1, "ZMW": 1, "ZWL": 1}

        actual_currency_usages_dict = {}
        for i in res_dict:
            actual_currency_usages_dict[i['code']] = i['usages']
            self.assertEqual(i['usages'], len(i['countries']),
                             'Unexpected length of the countries array in the response JSON')

        for (k, v), (k2, v2) in zip(actual_currency_usages_dict.items(), expected_currency_usages_dict.items()):
            self.assertEqual(k, k2,
                             "Unexpected currency code ordering")
            self.assertEqual(v, v2,
                             "Unexpected usages value for currency code")

if __name__ == "__main__":
    unittest.main()
