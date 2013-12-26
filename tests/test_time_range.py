from datetime import date, datetime, time, timedelta
from unittest import TestCase

from datetime_periods import TimeRange
from dateutil.tz import tzutc


class TimeRangeTest(TestCase):
    def setUp(self):
        self.now = datetime.now()
        self.date = self.now.date()
        self.start, self.stop = time(17), time(23)

    def combine(self, time, add_day=False, tzinfo=None):
        timestamp = datetime.combine(self.date, time)
        if tzinfo:
            timestamp = timestamp.replace(tzinfo=tzinfo)

        if add_day:
            return timestamp + timedelta(days=1)
        else:
            return timestamp

    def test_simple_times_after_each_other_should_work(self):
        start, stop = time(19), time(23, 30)

        tr = TimeRange(start, stop)
        self.assertEqual(tr.start, self.combine(start))
        self.assertEqual(tr.stop, self.combine(stop))

    def test_simple_times_where_stop_reaches_into_tomorrow_should_work(self):
        start, stop = time(17), time(1)

        tr = TimeRange(start, stop)
        self.assertEqual(tr.start, self.combine(start))
        self.assertEqual(tr.stop, self.combine(stop, add_day=True))

    def test_same_time_on_both_start_stop_should_end_tomorrow(self):
        start, stop = time(0), time(0)

        tr = TimeRange(start, stop)
        self.assertEqual(tr.start, self.combine(start))
        self.assertEqual(tr.stop, self.combine(stop, add_day=True))

    def test_time_should_be_passable_as_a_string(self):
        tr = TimeRange('17:00', '23:00')
        self.assertEqual(tr.start, self.combine(self.start))
        self.assertEqual(tr.stop, self.combine(self.stop))

    def test_date_should_be_passable_as_string(self):
        tr = TimeRange('17:00', '23:00', '2013-12-25')
        self.date = date(2013, 12, 25)
        self.assertEqual(tr.start, self.combine(self.start))
        self.assertEqual(tr.stop, self.combine(self.stop))

    def test_date_should_be_passable_as_date(self):
        tr = TimeRange('17:00', '23:00', self.now.date())
        self.assertEqual(tr.start, self.combine(self.start))
        self.assertEqual(tr.stop, self.combine(self.stop))

    def test_should_set_tzinfo_to_correct(self):
        tr = TimeRange(self.start, self.stop, tzinfo=tzutc())
        self.assertEqual(tr.start, self.combine(self.start, tzinfo=tzutc()))
        self.assertEqual(tr.stop, self.combine(self.stop, tzinfo=tzutc()))

        # It should just set the timezone, not convert between timezones
        self.assertEqual(tr.start.time(), self.start)
        self.assertEqual(tr.stop.time(), self.stop)

    def test_class_should_be_accessible_as_list(self):
        # Where 0=start, 1=stop
        tr = TimeRange(self.start, self.stop)
        self.assertEqual(tr[0], self.combine(self.start))
        self.assertEqual(tr[1], self.combine(self.stop))

    def test_class_should_not_allow_other_values_than_01_for_list_access(self):
        tr = TimeRange(self.start, self.stop)

        # assertRaises is not available as a context manager in 2.6,
        # so lets be creative.
        self.assertRaises(KeyError, lambda k: tr[k], -1)
        self.assertRaises(KeyError, lambda k: tr[k], 2)

    def test_should_allow_splatting_keys_for_the_timestamps(self):
        tr = TimeRange(self.start, self.stop)
        start, stop = tr

        self.assertEqual(start, self.combine(self.start))
        self.assertEqual(stop, self.combine(self.stop))

    def test___repr___should_show_reasonable_info_to_reproduce(self):
        tr = TimeRange(self.start, self.stop, '2013-12-25')
        self.assertEqual(
            tr.__repr__(),
            'TimeRange(start=datetime.time(17, 0), '
            'stop=datetime.time(23, 0), '
            'date=datetime.date(2013, 12, 25), tzinfo=None)'
        )
