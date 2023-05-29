import unittest

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

    def test_record_counts_join_table(self):
        cur = self.get_cursor()
        cur.execute("SELECT COUNT(*) FROM hackajob_global_currencies.country_currency")
        count = cur.fetchone()
        self.assertEqual(count[0], 268, 'The record count in the country_currency join table is NOT as expected')
        cur.close()

    @classmethod
    def tearDown(cls):
        # cls.cur.close()
        if cls.conn is not None and cls.conn.status == psycopg2.extensions.STATUS_READY:
            cls.conn.close()


if __name__ == "__main__":
    unittest.main()