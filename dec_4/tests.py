from unittest import TestCase
from .dec_4 import find_all_xmas_instances

SAMPLE_INPUT = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


class Test(TestCase):
    def test_find_all_xmas_instances(self):
        result = find_all_xmas_instances(SAMPLE_INPUT)
        self.assertEqual(result, 18, f"Expected 18, but got {result}")
