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

    def test_sample_currency_records(self):
        cur = self.get_cursor()
        cur.execute("SELECT code, name "
                    "FROM hackajob_global_currencies.currency ORDER BY code")
        result = cur.fetchall()
        col_names = []
        for e in cur.description:
            col_names.append(e[0])

        df = pandas.DataFrame(result, columns=col_names)
        self.assertEqual(df['code'][0], 'AED',
                         'Some expected data in the code column not found in currency table')
        self.assertEqual(df['name'][0], 'United Arab Emirates dirham',
                         'Some expected data in the name column not found in currency table')

        self.assertEqual(df['code'][1], 'AFN',
                         'Some expected data in the code column not found in currency table')
        self.assertEqual(df['name'][1], 'Afghan afghani',
                         'Some expected data in the name column not found in the currency table')

        self.assertEqual(df['code'][161], 'ZWL',
                         'Some expected data in the code column not found in currency table')
        self.assertEqual(df['name'][161], 'Zimbabwean dollar',
                         'Some expected data in the name column not found in currency table')

        cur.close()

    @classmethod
    def tearDown(cls):
        # cls.cur.close()
        if cls.conn is not None and cls.conn.status == psycopg2.extensions.STATUS_READY:
            cls.conn.close()


if __name__ == "__main__":
    unittest.main()