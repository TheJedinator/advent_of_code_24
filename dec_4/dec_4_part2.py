def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def check_x_mas(i, j):
        # Check for 'A' at the center
        if grid[i][j] != "A":
            return False

        patterns = [
            [(-1, -1, "M"), (-1, 1, "S"), (1, -1, "M"), (1, 1, "S")],  # Forward
            [(-1, -1, "S"), (-1, 1, "M"), (1, -1, "S"), (1, 1, "M")],  # Backward
        ]

        for pattern in patterns:
            if all(
                0 <= i + di < rows
                and 0 <= j + dj < cols
                and grid[i + di][j + dj] == char
                for di, dj, char in pattern
            ):
                return True
        return False

    for i in range(rows):
        for j in range(cols):
            if check_x_mas(i, j):
                count += 1

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
sample_grid = [line for line in SAMPLE_INPUT.strip().split("\n")]
grid = [line for line in open("dec_4/dec_4.input", "r").read().strip().split("\n")]
# Count X-MAS occurrences
result = count_x_mas(sample_grid)
print(f"X-MAS appears {result} times in the word search.")
