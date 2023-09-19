# test_number_range_analysis.py

import io
from unittest import mock, TestCase
from number_range_analysis import calculate_sum, find_smallest_number, find_largest_number, count_even_numbers, count_odd_numbers

class TestNumberRangeAnalysis(TestCase):

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_sum(self, mock_stdout):
        # Test case: Calculate the sum of numbers within a range.
        result = calculate_sum(1, 5)
        self.assertEqual(result, 15)
      

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_find_smallest_number(self, mock_stdout):
        # Test case: Find the smallest number within a range.
        result = find_smallest_number(3, 9)
        self.assertEqual(result, 3)
       

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_find_largest_number(self, mock_stdout):
        # Test case: Find the largest number within a range.
        result = find_largest_number(10, 20)
        self.assertEqual(result, 20)
      

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_count_even_numbers(self, mock_stdout):
        # Test case: Count the number of even numbers within a range.
        result = count_even_numbers(1, 10)
        self.assertEqual(result, 5)
        

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_count_odd_numbers(self, mock_stdout):
        # Test case: Count the number of odd numbers within a range.
        result = count_odd_numbers(15, 25)
        self.assertEqual(result, 6)
        

if __name__ == '__main__':
    unittest.main()
