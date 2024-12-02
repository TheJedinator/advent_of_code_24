def read_file_to_reports(filename: str):
    with open(filename, "r") as f:
        lines = f.readlines()
    reports = []
    for line in lines:
        report = line.strip().split(" ")
        reports.append(report)
    return reports


class Report:
    def __init__(self, report: list[str]):
        self.report = [int(r) for r in report]

    def is_increasing(self):
        for i in range(1, len(self.report)):
            if self.report[i] <= self.report[i - 1]:
                return False
        return True

    def is_decreasing(self):
        for i in range(1, len(self.report)):
            if self.report[i] >= self.report[i - 1]:
                return False
        return True

    def is_safe(self):
        return (
            self.is_increasing() or self.is_decreasing()
        ) and self.greatest_distance_between_neighbours() <= 3

    def greatest_distance_between_neighbours(self):
        max_diff = 0
        for i in range(1, len(self.report)):
            diff = abs(self.report[i] - self.report[i - 1])
            if diff > max_diff:
                max_diff = diff
        return max_diff

    def problem_dampner(self):
        """The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

        The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

        Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

        More of the above example's reports are now safe:

        7 6 4 2 1: Safe without removing any level.
        1 2 7 8 9: Unsafe regardless of which level is removed.
        9 7 6 2 1: Unsafe regardless of which level is removed.
        1 3 2 4 5: Safe by removing the second level, 3.
        8 6 4 4 1: Safe by removing the third level, 4.
        1 3 6 7 9: Safe without removing any level.
        Thanks to the Problem Dampener, 4 reports are actually safe!

        Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?"""
        # return the dampned set
        # if by removing one element we are decreasing or increasing, return the amended report
        # if not, return the original report
        if not self.is_safe():
            # if we pop any element and the report is now increasing or decreasing, return the report
            for i in range(len(self.report)):
                report = self.report.copy()
                report.pop(i)
                if (
                    Report(report).is_increasing() or Report(report).is_decreasing()
                ) and Report(report).greatest_distance_between_neighbours() <= 3:
                    return Report(report)

        return self


if __name__ == "__main__":
    reports = read_file_to_reports("dec2_input.txt")
    safe_reports = [r for r in reports if Report(r).problem_dampner().is_safe()]
    print(len(safe_reports))
