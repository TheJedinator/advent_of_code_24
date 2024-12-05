import re


def find_xmas(line):
    return len(re.findall(r"(?=XMAS|SAMX)", line))


def get_diagonals(grid):
    height, width = len(grid), len(grid[0])
    diagonals = []

    # Main diagonals
    for i in range(height + width - 1):
        diagonal = "".join(
            grid[row][col]
            for row, col in zip(
                range(max(0, i - width + 1), min(height, i + 1)),
                range(min(i, width - 1), max(-1, i - height), -1),
            )
        )
        diagonals.append(diagonal)

    # Anti-diagonals
    for i in range(height + width - 1):
        anti_diagonal = "".join(
            grid[row][col]
            for row, col in zip(
                range(max(0, i - width + 1), min(height, i + 1)),
                range(max(0, width - i - 1), min(width, height + width - i - 1)),
            )
        )
        diagonals.append(anti_diagonal)

    return diagonals


def count_xmas(grid):
    count = 0

    # Check rows
    for row in grid:
        count += find_xmas(row)

    # Check columns
    for col in zip(*grid):
        count += find_xmas("".join(col))

    # Check diagonals
    for diagonal in get_diagonals(grid):
        count += find_xmas(diagonal)

    return count


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
grid = [line for line in open("dec_4/dec_4.input", "r").read().strip().split("\n")]
# grid = [line for line in SAMPLE_INPUT.strip().split("\n")]
# Count XMAS occurrences
result = count_xmas(grid)
print(f"XMAS appears {result} times in the word search.")
