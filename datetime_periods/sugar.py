from datetime_truncate import truncate

from .period import period
from .period_end import period_end


def period_second(datetime):
    ''' Sugar for :py:func:`period(datetime, 'second')` '''
    return period(datetime, 'second')


def period_minute(datetime):
    ''' Sugar for :py:func:`period(datetime, 'minute')` '''
    return period(datetime, 'minute')


def period_hour(datetime):
    ''' Sugar for :py:func:`period(datetime, 'hour')` '''
    return period(datetime, 'hour')


def period_day(datetime):
    ''' Sugar for :py:func:`period(datetime, 'day')` '''
    return period(datetime, 'day')


def period_week(datetime):
    ''' Sugar for :py:func:`period(datetime, 'week')` '''
    return period(datetime, 'week')


def period_month(datetime):
    ''' Sugar for :py:func:`period(datetime, 'month')` '''
    return period(datetime, 'month')


def period_quarter(datetime):
    ''' Sugar for :py:func:`period(datetime, 'quarter')` '''
    return period(datetime, 'quarter')


def period_half_year(datetime):
    ''' Sugar for :py:func:`period(datetime, 'half')` '''
    return period(datetime, 'half_year')


def period_year(datetime):
    ''' Sugar for :py:func:`period(datetime, 'year')` '''
    return period(datetime, 'year')


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


def period_beginning_second(datetime):
    ''' Sugar for :py:func:`datetime_truncate.truncate(datetime, 'second')` '''
    return truncate(datetime, 'second')


def period_beginning_minute(datetime):
    ''' Sugar for :py:func:`datetime_truncate.truncate(datetime, 'minute')` '''
    return truncate(datetime, 'minute')


def period_beginning_hour(datetime):
    ''' Sugar for :py:func:`datetime_truncate.truncate(datetime, 'hour')` '''
    return truncate(datetime, 'hour')


def period_beginning_day(datetime):
    ''' Sugar for :py:func:`datetime_truncate.truncate(datetime, 'day')` '''
    return truncate(datetime, 'day')


def period_beginning_week(datetime):
    ''' Sugar for :py:func:`datetime_truncate.truncate(datetime, 'week')` '''
    return truncate(datetime, 'week')


def period_beginning_month(datetime):
    ''' Sugar for :py:func:`datetime_truncate.truncate(datetime, 'month')` '''
    return truncate(datetime, 'month')


def period_beginning_quarter(datetime):
    '''
    Sugar for :py:func:`datetime_truncate.truncate(datetime, 'quarter')`
    '''
    return truncate(datetime, 'quarter')


def period_beginning_half_year(datetime):
    ''' Sugar for :py:func:`datetime_truncate.truncate(datetime, 'half')` '''
    return truncate(datetime, 'half_year')


def period_beginning_year(datetime):
    ''' Sugar for :py:func:`datetime_truncate.truncate(datetime, 'year')` '''
    return truncate(datetime, 'year')
