from unittest import TestCase
from dec_5 import get_print_jobs, get_priorities
from dec_5 import sort_job_by_priorities
from dec_5 import solve

REQUIRED_ORDERING_SAMPLE = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13
"""

UPDATES_TO_PRINT_SAMPLE = """
75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


class TestDec5(TestCase):
    def test_required_ordering(self):
        ordering = get_priorities(REQUIRED_ORDERING_SAMPLE)
        self.assertEqual(ordering[0], (47, 53))

    def test_page_updates(self):
        expected = [75, 47, 61, 53, 29]
        updates = get_print_jobs(UPDATES_TO_PRINT_SAMPLE)
        self.assertEqual(updates[0], expected)

    def test_sort_job_by_priorities(self):
        ordering = get_priorities(REQUIRED_ORDERING_SAMPLE)
        job = [75, 97, 47, 61, 53]
        reorderd_job, _ = sort_job_by_priorities(job, ordering)
        expected_job_order = [97, 75, 47, 61, 53]
        self.assertEqual(reorderd_job, expected_job_order)

        second_job = [61, 13, 29]
        reorderd_job, _ = sort_job_by_priorities(second_job, ordering)
        expected_job_order = [61, 29, 13]
        self.assertEqual(reorderd_job, expected_job_order)

    def test_solve(self):
        unmodified_result, modified_result = solve(
            REQUIRED_ORDERING_SAMPLE, UPDATES_TO_PRINT_SAMPLE
        )
        self.assertEqual(unmodified_result, 143)
        self.assertEqual(modified_result, 123)
