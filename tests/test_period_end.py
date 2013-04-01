from datetime import datetime
import unittest

from datetime_periods import period_end


class TestPeriodEnd(unittest.TestCase):
    def test_period_end_second(self):
        beginning = datetime(2012, 4, 2)
        self.assertEqual(period_end(beginning, 'second'),
                         datetime(2012, 4, 2, 0, 0, 0, 999999))

    def test_period_end_minute(self):
        beginning = datetime(2012, 4, 2)
        self.assertEqual(period_end(beginning, 'minute'),
                         datetime(2012, 4, 2, 0, 0, 59))

    def test_period_end_hour(self):
        beginning = datetime(2012, 4, 2)
        self.assertEqual(period_end(beginning, 'hour'),
                         datetime(2012, 4, 2, 0, 59, 59))

    def test_period_end_day(self):
        beginning = datetime(2012, 4, 2)
        self.assertEqual(period_end(beginning, 'day'),
                         datetime(2012, 4, 2, 23, 59, 59))

    def test_period_end_week(self):
        beginning = datetime(2012, 4, 2)
        self.assertEqual(period_end(beginning, 'week'),
                         datetime(2012, 4, 8, 23, 59, 59))

    def test_period_end_month(self):
        beginning = datetime(2012, 4, 1)
        self.assertEqual(period_end(beginning, 'month'),
                         datetime(2012, 4, 30, 23, 59, 59))

    def test_period_end_quarter(self):
        beginning = datetime(2012, 4, 1)
        self.assertEqual(period_end(beginning, 'quarter'),
                         datetime(2012, 6, 30, 23, 59, 59))

    def test_period_end_half_year(self):
        beginning = datetime(2012, 7, 1)
        self.assertEqual(period_end(beginning, 'half_year'),
                         datetime(2012, 12, 31, 23, 59, 59))

    def test_period_end_year(self):
        beginning = datetime(2012, 1, 1)
        self.assertEqual(period_end(beginning, 'year'),
                         datetime(2012, 12, 31, 23, 59, 59))
