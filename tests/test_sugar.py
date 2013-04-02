from datetime import datetime
import unittest

from datetime_periods import sugar


class TestSugarFunctions(unittest.TestCase):
    def test_all_of_them(self):
        '''
        Since the sugar methods have all been tested on their own the logic
        of them should be sound. But to ensure that a typo made it so that
        they don't work at all let's just iterate over them and send in a
        datetime to see if no exceptions are raised.
        '''
        test_datetime = datetime(2012, 3, 1)
        for function in dir(sugar):
            if function.startswith('_'): continue

            getattr(sugar, function)(test_datetime)
