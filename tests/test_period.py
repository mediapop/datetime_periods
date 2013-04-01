from datetime import datetime
import unittest

from datetime_periods import period


class TestPeriod(unittest.TestCase):
    def test_period_second(self):
        beginning = datetime(2012, 4, 1, microsecond=5000)
        self.assertEqual(period(beginning, 'second'),
                         [datetime(2012, 4, 1, microsecond=0),
                          datetime(2012, 4, 1, microsecond=999999)])

    def test_period_minute(self):
        beginning = datetime(2012, 4, 2, second=12)
        self.assertEqual(period(beginning, 'minute'),
                         [datetime(2012, 4, 2),
                          datetime(2012, 4, 2, 0, 0, 59)])

    def test_period_hour(self):
        beginning = datetime(2012, 4, 2, minute=20)
        self.assertEqual(period(beginning, 'hour'),
                         [datetime(2012, 4, 2),
                          datetime(2012, 4, 2, 0, 59, 59)])

    def test_period_day(self):
        beginning = datetime(2012, 4, 2, hour=12)
        self.assertEqual(period(beginning, 'day'),
                         [datetime(2012, 4, 2),
                          datetime(2012, 4, 2, 23, 59, 59)])

    def test_period_week(self):
        beginning = datetime(2012, 4, 3)
        self.assertEqual(period(beginning, 'week'),
                         [datetime(2012, 4, 2),
                          datetime(2012, 4, 8, 23, 59, 59)])

    def test_period_month(self):
        beginning = datetime(2012, 4, 15)
        self.assertEqual(period(beginning, 'month'),
                         [datetime(2012, 4, 1),
                          datetime(2012, 4, 30, 23, 59, 59)])

    def test_period_quarter(self):
        beginning = datetime(2012, 5, 15)
        self.assertEqual(period(beginning, 'quarter'),
                         [datetime(2012, 4, 1),
                          datetime(2012, 6, 30, 23, 59, 59)])

    def test_period_half_year(self):
        beginning = datetime(2012, 9, 1)
        self.assertEqual(period(beginning, 'half_year'),
                         [datetime(2012, 7, 1),
                          datetime(2012, 12, 31, 23, 59, 59)])

    def test_period_year(self):
        beginning = datetime(2012, 7, 1)
        self.assertEqual(period(beginning, 'year'),
                         [datetime(2012, 1, 1),
                          datetime(2012, 12, 31, 23, 59, 59)])
