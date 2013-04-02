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


The `sugar` module has sugar functions for all variants available.

Sugar functions for entire period:

* `period_second`
* `period_minute`
* `period_hour`
* `period_day`
* `period_week`
* `period_month`
* `period_quarter`
* `period_half_year`
* `period_year`

Sugar functions for beginning of period:

* `period_beginning_second`
* `period_beginning_minute`
* `period_beginning_hour`
* `period_beginning_day`
* `period_beginning_week`
* `period_beginning_month`
* `period_beginning_quarter`
* `period_beginning_half_year`
* `period_beginning_year`

Sugar functions for end of period:

* `period_end_second`
* `period_end_minute`
* `period_end_hour`
* `period_end_day`
* `period_end_week`
* `period_end_month`
* `period_end_quarter`
* `period_end_half_year`
* `period_end_year`


:mod:`datetime_periods`
------------------------------------------

.. autofunction:: datetime_periods.period

.. autofunction:: datetime_periods.period_beginning
This function is an alias for `datetime_truncate.truncate`_.

.. _`datetime_truncate.truncate`: https://github.com/mediapop/datetime_truncate/

.. autofunction:: datetime_periods.period_end

.. automodule:: datetime_periods.period
    :members:

.. automodule:: datetime_periods.period_end
    :members:

.. automodule:: datetime_periods.sugar
    :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
