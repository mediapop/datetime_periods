================
datetime_periods
================


This module aims to help you create time periods as easily as if by a
snap of your finger.

Pass in a :py:mod:`datetime.datetime()` object and a period name and it'll
return the beginning and end of that period.

Usage:
------

    >>> from datetime_periods import period
    >>> period(datetime(2012, 4, 2, second=12), 'minute')
    [datetime(2012, 4, 2), datetime(2012, 4, 2, 0, 0, 59)]
    >>> period(datetime(2012, 4, 2), 'hour')
    [datetime(2012, 4, 2, 0), datetime(2012, 4, 2, 0, 59, 59)]
    >>> period(datetime(2012, 4, 2), 'day')
    [datetime(2012, 4, 2), datetime(2012, 4, 2, 23, 59, 59)]
    >>> period(datetime(2012, 4, 2), 'week')
    [datetime(2012, 4, 2), datetime(2012, 4, 8, 23, 59, 59)]
    >>> period(datetime(2012, 4, 15), 'month')
    [datetime(2012, 4, 1), datetime(2012, 4, 30, 23, 59, 59)]
    >>> period(datetime(2012, 4, 2), 'quarter')
    [datetime(2012, 4, 1), datetime(2012, 6, 30, 23, 59, 59)]
    >>> period(datetime(2012, 9, 1), 'half_year')
    [datetime(2012, 7, 1), datetime(2012, 12, 31, 23, 59, 59)]
    >>> period(datetime(2012, 7, 1), 'year')
    [datetime(2012, 1, 1), datetime(2012, 12, 31, 23, 59, 59)]


There are also sugar functions available on the form:

* `period_second`
* `period_minute`
* `period_hour`
* `period_day`
* `period_week`
* `period_month`
* `period_quarter`
* `period_half_year`
* `period_year`


:mod:`datetime_periods`
------------------------------------------

.. autofunction:: datetime_periods.period

.. autofunction:: datetime_periods.period_beginning
This function is an alias for `datetime_truncate.truncate`_.

.. _`datetime_truncate.truncate`: https://github.com/mediapop/datetime_truncate/

.. autofunction:: datetime_periods.period_end

.. automodule:: datetime_periods
    :members:

.. automodule:: datetime_periods.period
    :members:

.. automodule:: datetime_periods.period_end
    :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
