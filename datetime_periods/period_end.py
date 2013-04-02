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
    else:
        raise ValueError('{} is not a valid period_name. Valid: {}'.format(
            period_name,
            ', '.join(PERIODS.keys())
        ))
