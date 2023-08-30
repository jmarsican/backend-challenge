import unittest
from json import JSONDecodeError

import requests

__unittest = True


class TestEndpoint(unittest.TestCase):

    url = "http://localhost:8080/currencies/usage"

    @classmethod
    def setUp(cls):
        x = None

    def test_countries_array_values(self):
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

        expected_dict = {
            "EUR": ["CYP", "ALA", "LTU", "IRL", "GRC", "LVA", "FIN", "GUF", "ITA", "GLP", "MAF", "BEL", "MCO", "UNK",
                    "FRA", "MLT", "ESP", "SVK", "MTQ", "REU", "LUX", "ATF", "AND", "MNE", "BLM", "NLD", "DEU", "SVN",
                    "EST", "VAT", "SMR", "HRV", "PRT", "AUT", "MYT", "SPM"],
            "USD": ["GUM", "FSM", "KHM", "USA", "MNP", "SLV", "BES", "VGB", "TLS", "VIR", "IOT", "PLW", "PRI", "TCA",
                    "PAN", "MHL", "BHS", "ASM", "ECU", "UMI"],
            "XCD": ["KNA", "VCT", "GRD", "AIA", "DMA", "ATG", "MSR", "LCA"],
            "XOF": ["CIV", "BFA", "GNB", "NER", "MLI", "SEN", "BEN", "TGO"],
            "AUD": ["NFK", "TUV", "AUS", "CCK", "KIR", "NRU", "CXR"], "XAF": ["CMR", "GNQ", "TCD", "COG", "CAF", "GAB"],
            "GBP": ["GGY", "SHN", "JEY", "GBR", "IMN"], "NZD": ["NZL", "COK", "TKL", "PCN", "NIU"],
            "ZAR": ["LSO", "NAM", "SWZ", "ZAF"], "DKK": ["DNK", "FRO", "GRL"], "XPF": ["PYF", "WLF", "NCL"],
            "ANG": ["SXM", "CUW"], "CHF": ["LIE", "CHE"], "DZD": ["DZA", "ESH"], "EGP": ["PSE", "EGY"],
            "ILS": ["PSE", "ISR"], "INR": ["IND", "BTN"], "JOD": ["JOR", "PSE"], "MAD": ["ESH", "MAR"],
            "MRU": ["ESH", "MRT"], "NOK": ["SJM", "NOR"], "SGD": ["BRN", "SGP"], "SHP": ["SGS", "SHN"], "AED": ["ARE"],
            "AFN": ["AFG"], "ALL": ["ALB"], "AMD": ["ARM"], "AOA": ["AGO"], "ARS": ["ARG"], "AWG": ["ABW"],
            "AZN": ["AZE"], "BAM": ["BIH"], "BBD": ["BRB"], "BDT": ["BGD"], "BGN": ["BGR"], "BHD": ["BHR"],
            "BIF": ["BDI"], "BMD": ["BMU"], "BND": ["BRN"], "BOB": ["BOL"], "BRL": ["BRA"], "BSD": ["BHS"],
            "BTN": ["BTN"], "BWP": ["BWA"], "BYN": ["BLR"], "BZD": ["BLZ"], "CAD": ["CAN"], "CDF": ["COD"],
            "CKD": ["COK"], "CLP": ["CHL"], "CNY": ["CHN"], "COP": ["COL"], "CRC": ["CRI"], "CUC": ["CUB"],
            "CUP": ["CUB"], "CVE": ["CPV"], "CZK": ["CZE"], "DJF": ["DJI"], "DOP": ["DOM"], "ERN": ["ERI"],
            "ETB": ["ETH"], "FJD": ["FJI"], "FKP": ["FLK"], "FOK": ["FRO"], "GEL": ["GEO"], "GGP": ["GGY"],
            "GHS": ["GHA"], "GIP": ["GIB"], "GMD": ["GMB"], "GNF": ["GIN"], "GTQ": ["GTM"], "GYD": ["GUY"],
            "HKD": ["HKG"], "HNL": ["HND"], "HTG": ["HTI"], "HUF": ["HUN"], "IDR": ["IDN"], "IMP": ["IMN"],
            "IQD": ["IRQ"], "IRR": ["IRN"], "ISK": ["ISL"], "JEP": ["JEY"], "JMD": ["JAM"], "JPY": ["JPN"],
            "KES": ["KEN"], "KGS": ["KGZ"], "KHR": ["KHM"], "KID": ["KIR"], "KMF": ["COM"], "KPW": ["PRK"],
            "KRW": ["KOR"], "KWD": ["KWT"], "KYD": ["CYM"], "KZT": ["KAZ"], "LAK": ["LAO"], "LBP": ["LBN"],
            "LKR": ["LKA"], "LRD": ["LBR"], "LSL": ["LSO"], "LYD": ["LBY"], "MDL": ["MDA"], "MGA": ["MDG"],
            "MKD": ["MKD"], "MMK": ["MMR"], "MNT": ["MNG"], "MOP": ["MAC"], "MUR": ["MUS"], "MVR": ["MDV"],
            "MWK": ["MWI"], "MXN": ["MEX"], "MYR": ["MYS"], "MZN": ["MOZ"], "NAD": ["NAM"], "NGN": ["NGA"],
            "NIO": ["NIC"], "NPR": ["NPL"], "OMR": ["OMN"], "PAB": ["PAN"], "PEN": ["PER"], "PGK": ["PNG"],
            "PHP": ["PHL"], "PKR": ["PAK"], "PLN": ["POL"], "PYG": ["PRY"], "QAR": ["QAT"], "RON": ["ROU"],
            "RSD": ["SRB"], "RUB": ["RUS"], "RWF": ["RWA"], "SAR": ["SAU"], "SBD": ["SLB"], "SCR": ["SYC"],
            "SDG": ["SDN"], "SEK": ["SWE"], "SLL": ["SLE"], "SOS": ["SOM"], "SRD": ["SUR"], "SSP": ["SSD"],
            "STN": ["STP"], "SYP": ["SYR"], "SZL": ["SWZ"], "THB": ["THA"], "TJS": ["TJK"], "TMT": ["TKM"],
            "TND": ["TUN"], "TOP": ["TON"], "TRY": ["TUR"], "TTD": ["TTO"], "TVD": ["TUV"], "TWD": ["TWN"],
            "TZS": ["TZA"], "UAH": ["UKR"], "UGX": ["UGA"], "UYU": ["URY"], "UZS": ["UZB"], "VES": ["VEN"],
            "VND": ["VNM"], "VUV": ["VUT"], "WST": ["WSM"], "YER": ["YEM"], "ZMW": ["ZMB"], "ZWL": ["ZWE"]}

        actual_dict = {}
        for i in res_dict:
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