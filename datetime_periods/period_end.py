from dateutil.relativedelta import relativedelta

PERIODS = {
    'second': dict(seconds=1, microseconds=-1),
    'minute': dict(minutes=1, seconds=-1),
    'hour': dict(hours=1, seconds=-1),
    'day': dict(days=1, seconds=-1),
    'week': dict(weeks=1, seconds=-1),
    'month': dict(months=1, seconds=-1),
    'quarter': dict(months=3, seconds=-1),
    'half_year': dict(months=6, seconds=-1),
    'year': dict(years=1, seconds=-1),
}


def period_end(datetime, period_name='day'):
    '''
    Returns a datetime where it is the end of `period_name`.
    Notice that :py:func:`period_end()` assumes that the `datetime` has
    been run by :py:func:`truncate()` before being passed in. If that
    is not the case the results might not be what is expected.

    Possible values for `period_name`:

    * second
    * minute
    * hour
    * day
    * week (iso week i.e. monday to sunday)
    * month
    * quarter
    * half_year
    * year

    Examples::

        >>> period_end(datetime(2012, 4, 2), 'hour')
        datetime(2012, 4, 2, 0, 59, 59)
        >>> period_end(datetime(2012, 4, 2), 'day')
        datetime(2012, 4, 2, 23, 59, 59)
        >>> period_end(datetime(2012, 4, 2), 'week')
        datetime(2012, 4, 8, 23, 59, 59)
        >>> period_end(datetime(2012, 4, 1), 'quarter')
        datetime(2012, 6, 30, 23, 59, 59)

    :params datetime: A truncated datetime object
    :params period_name: The period for which to calculate the end for
                         `datetime`
    :return: datetime with all fields to second set to the very last before
             before the next period
    :rtype: :py:mod:`datetime` datetime object
    '''
    if period_name in PERIODS:
        return datetime + relativedelta(**PERIODS[period_name])


def period_end_second(datetime):
    ''' Sugar for :py:func:`period_end(datetime, 'second')` '''
    return period_end(datetime, 'second')


def period_end_minute(datetime):
    ''' Sugar for :py:func:`period_end(datetime, 'minute')` '''
    return period_end(datetime, 'minute')


def period_end_hour(datetime):
    ''' Sugar for :py:func:`period_end(datetime, 'hour')` '''
    return period_end(datetime, 'hour')


def period_end_day(datetime):
    ''' Sugar for :py:func:`period_end(datetime, 'day')` '''
    return period_end(datetime, 'day')


def period_end_week(datetime):
    ''' Sugar for :py:func:`period_end(datetime, 'week')` '''
    return period_end(datetime, 'week')


def period_end_month(datetime):
    ''' Sugar for :py:func:`period_end(datetime, 'month')` '''
    return period_end(datetime, 'month')


def period_end_quarter(datetime):
    ''' Sugar for :py:func:`period_end(datetime, 'quarter')` '''
    return period_end(datetime, 'quarter')


def period_end_half_year(datetime):
    ''' Sugar for :py:func:`period_end(datetime, 'half')` '''
    return period_end(datetime, 'half_year')


def period_end_year(datetime):
    ''' Sugar for :py:func:`period_end(datetime, 'year')` '''
    return period_end(datetime, 'year')
