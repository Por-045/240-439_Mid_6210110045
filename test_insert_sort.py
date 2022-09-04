from insert_sort import insertion_sort

import unittest

class InsertSortTest(unittest.TestCase):
    def test_give_5_2_6_should_2_5_6(self):
        number = [5, 2, 6]
        excepted_result = [2, 5, 6]

        result = insertion_sort(number)

        self.assertEqual(result, excepted_result)

    def test_give_156_54_minus20_65_minus532_should_minus532_minus20_54_65_156(self):
        number = [156, 54, -20, 65, -532]
        excepted_result = [-532, -20, 54, 65, 156]

        result = insertion_sort(number)

        self.assertEqual(result, excepted_result)