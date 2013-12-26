from datetime import datetime, timedelta

from dateutil.parser import parse
import six


class TimeRange(object):
    """Takes two times, ``start`` and ``stop``, and tries to be
    smart about putting a date to those times.

    Stop is always assumed to follow start in chronological order, so
    if stop is numerically less than start then it must be tomorrow.

    Strings are parsed with ``dateutil.parser`` from the
    `python-dateutil` package.

    This class can also act like a 2 length list where index 0=start,
    1=stop time. This to allow the class to be used for argument
    expansion and as an iterator.

    Examples::

        >>> tr = TimeRange('17:00', '23:00', '2013-12-25')
        >>> tr.start
        datetime(2013, 12, 25, 17)
        >>> tr.stop
        datetime(2013, 12, 25, 23)
        >>> tr = TimeRange('17:00', '04:00', '2013-12-25')
        >>> tr.start
        datetime(2013, 12, 25, 17)
        >>> tr.stop
        datetime(2013, 12, 26, 4)
        >>> tr[0] == tr.start
        True
        >>> tr[1] == tr.stop
        True

    :param start: a ``time`` object or a time string
    :param stop: a ``time`` object or a time string
    :param date: a ``datetime``, ``date``, or date string
    :param tzinfo: None or a tzinfo that will replace the current one
                   in the ``timestamp`` attributes ``start`` and ``stop``

    """
    def __init__(self, start, stop, date=None, tzinfo=None):
        self.date = self._ensure_date(date)
        self.tzinfo = tzinfo

        self.time = {
            'start': self._ensure_time(start),
            'stop': self._ensure_time(stop),
        }

        self._timestamps()

    def _timestamps(self):
        self.timestamp = {}
        start, stop = self.time['start'], self.time['stop']

        self.timestamp['start'] = datetime.combine(self.date, start)
        self.timestamp['stop'] = datetime.combine(self.date, stop)

        if stop <= start:
            self.timestamp['stop'] = self.timestamp['stop'] + timedelta(days=1)

        if self.tzinfo:
            for k, v in self.timestamp.items():
                self.timestamp[k] = v.replace(tzinfo=self.tzinfo)

    def _ensure_date(self, date):
        if not date:
            date = datetime.now()
        elif isinstance(date, six.string_types):
            date = parse(date, yearfirst=True)  # ISO8601 dates ftw

        try:
            return date.date()
        except AttributeError:
            return date

    def _ensure_time(self, timestamp):
        if isinstance(timestamp, six.string_types):
            timestamp = parse(timestamp)

        try:
            return timestamp.time()
        except AttributeError:
            return timestamp

    def __getitem__(self, key):
        if key == 0:
            return self.start
        elif key == 1:
            return self.stop
        else:
            raise KeyError

    def __iter__(self):
        return iter((self.start, self.stop))

    def __repr__(self):
        return('{cls}(start={start}, stop={stop}, '
               'date={date}, tzinfo={tzinfo})').format(
            cls=self.__class__.__name__,
            start=self.time['start'].__repr__(),
            stop=self.time['stop'].__repr__(),
            date=self.date.__repr__(),
            tzinfo=self.tzinfo.__repr__(),
        )

    @property
    def start(self):
        """The inserted ``start`` as a timestamp, if ``tzinfo`` was passed in
        it'll be set
        """
        return self.timestamp['start']

    @property
    def stop(self):
        """The inserted ``stop`` as a timestamp, if ``tzinfo`` was passed in
        it'll be set
        """
        return self.timestamp['stop']
