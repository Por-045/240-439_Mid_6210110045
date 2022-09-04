from insert_sort import insertion_sort

import unittest

class InsertSortTest(unittest.TestCase):
    def test_give_5_2_6_should_2_5_6(self):
        number = [5, 2, 6]
        excepted_result = [2, 5, 6]

        result = insertion_sort(number)

        self.assertEqual(result, excepted_result)