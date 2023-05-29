import unittest

import pandas
import psycopg2
import psycopg2.extensions

__unittest = True


class TestDatabaseData(unittest.TestCase):

    conn = None

    @classmethod
    def setUp(cls):
        cls.conn = psycopg2.connect("dbname=postgres user=postgres password=password host=localhost port=5432")

    def get_cursor(self):
        return self.conn.cursor()

    def test_sample_country_records(self):
        cur = self.get_cursor()
        cur.execute("SELECT cca3, official_name, common_name "
                    "FROM hackajob_global_currencies.country ORDER BY cca3")
        result = cur.fetchall()
        col_names = []
        for e in cur.description:
            col_names.append(e[0])

        df = pandas.DataFrame(result, columns=col_names)
        self.assertEqual(df['cca3'][0], 'ABW',
                         'Some expected data in the cca3 column not found in country table')

        self.assertEqual(df['cca3'][1], 'AFG',
                         'Some expected data in the cca3 column not found in country table')
        self.assertEqual(df['common_name'][1], 'Afghanistan',
                         'Some expected data in the common_name column not found in country table')
        self.assertEqual(df['official_name'][1], 'Islamic Republic of Afghanistan',
                         'Some expected data in the official_name column not found in the country table')

        self.assertEqual(df['cca3'][249], 'ZWE',
                         'Some expected data in the cca3 column not found in country table')
        self.assertEqual(df['common_name'][249], 'Zimbabwe',
                         'Some expected data in the common_name column not found in country table')
        self.assertEqual(df['official_name'][249], 'Republic of Zimbabwe',
                         'Some expected data in the official_name column not found in the country table')

        cur.close()

    @classmethod
    def tearDown(cls):
        # cls.cur.close()
        if cls.conn is not None and cls.conn.status == psycopg2.extensions.STATUS_READY:
            cls.conn.close()


if __name__ == "__main__":
    unittest.main()