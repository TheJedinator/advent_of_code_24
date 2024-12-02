from unittest import TestCase
from dec2_code import (
    biggest_number_difference_sequentially,
    numbers_increasing,
    numbers_decreasing,
    report_is_safe,
)  # noqa


class TestDec2(TestCase):
    def test_increasing_is_increasing(self):
        increasing_numbers = [1, 2, 3, 4]
        self.assertTrue(numbers_increasing(increasing_numbers))

    def test_decreasing_is_not_increasing(self):
        decreasing_numbers = [4, 3, 2, 1]
        self.assertFalse(numbers_increasing(decreasing_numbers))

    def test_mixed_is_not_increasing(self):
        mixed_numbers = [1, 2, 1, 2]
        self.assertFalse(numbers_increasing(mixed_numbers))

    def test_decreasing_is_decreasing(self):
        decreasing_numbers = [4, 3, 2, 1]
        self.assertTrue(numbers_decreasing(decreasing_numbers))

    def test_increasing_is_not_decreasing(self):
        increasing_numbers = [1, 2, 3, 4]
        self.assertFalse(numbers_decreasing(increasing_numbers))

    def test_mixed_is_not_decreasing(self):
        mixed_numbers = [1, 2, 1, 2]
        self.assertFalse(numbers_decreasing(mixed_numbers))

    def test_max_diff_sequentially(self):
        numbers = [1, 2, 3, 4]
        self.assertEqual(1, biggest_number_difference_sequentially(numbers))

    def test_max_diff_sequentially_mixed(self):
        numbers = [1, 20, 4, 9]
        self.assertEqual(19, biggest_number_difference_sequentially(numbers))

    def test_max_diff_sequentially_decreasing(self):
        numbers = [52, 45, 43, 50]
        self.assertEqual(7, biggest_number_difference_sequentially(numbers))

    def test_increase_same_number_false(self):
        numbers = [1, 1, 1, 1]
        self.assertFalse(numbers_increasing(numbers))

    def test_decrease_same_number_false(self):
        numbers = [1, 1, 1, 1]
        self.assertFalse(numbers_decreasing(numbers))

    def test_should_be_safe_is_safe(self):
        report = [1, 2, 3, 4]
        self.assertTrue(report_is_safe(report))

    def test_should_be_safe_is_safe_decreasing(self):
        report = [4, 3, 2, 1]
        self.assertTrue(report_is_safe(report))

    def test_difference_at_three_safe_increasing(self):
        report = [1, 3, 6, 9]
        self.assertTrue(report_is_safe(report))

    def test_difference_at_three_safe_decreasing(self):
        report = [9, 6, 3, 1]
        self.assertTrue(report_is_safe(report))

    def test_difference_above_three_unsafe_increasing(self):
        report = [1, 4, 8, 12]
        self.assertFalse(report_is_safe(report))

    def test_difference_above_three_unsafe_decreasing(self):
        report = [12, 8, 4, 1]
        self.assertFalse(report_is_safe(report))
