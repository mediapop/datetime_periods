from datetime_truncate import truncate as period_beginning
from .period_end import period_end


def period(datetime, period_name='day'):
    '''
    Takes the given `datetime` and then creates the `period_name` that
    `datetime` belongs to. If given one in the middle of the day and
    `period_name` 'day' then it'll be from 00:00:00 till 23:59:59.

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

        >>> period(datetime(2012, 4, 2), 'hour')
        [datetime(2012, 4, 2, 0), datetime(2012, 4, 2, 0, 59, 59)]
        >>> period(datetime(2012, 4, 2), 'day')
        [datetime(2012, 4, 2), datetime(2012, 4, 2, 23, 59, 59)]
        >>> period(datetime(2012, 4, 2), 'week')
        [datetime(2012, 4, 2), datetime(2012, 4, 8, 23, 59, 59)]
        >>> period(datetime(2012, 4, 2), 'quarter')
        [datetime(2012, 4, 1), datetime(2012, 6, 30, 23, 59, 59)]

    :params datetime: A truncated datetime object
    :params period_name: The period for which to calculate the end for
                         `datetime`
    :return: datetime with all fields to second set to the very last before
             before the next period
    :rtype: :py:mod:`datetime` datetime object
    '''
    start = period_beginning(datetime, period_name)
    return [start,
            period_end(start, period_name)]
