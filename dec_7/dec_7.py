from itertools import product
import math


MULTIPLY = "*"
ADD = "+"
COMBINE = "||"


def get_input(path: str):
    with open(path, "r") as f:
        return f.read().splitlines()


def get_equation_and_result(line: str) -> tuple[list[int], int]:
    result, equation = line.split(":")
    result = int(result)
    equation = [int(x) for x in equation.split()]
    return equation, result


def evaluate_expression(equation: list[int], operators: tuple[str, ...]) -> int:
    result = equation[0]
    for i, operator in enumerate(operators):
        if operator == ADD:
            result += equation[i + 1]
        elif operator == MULTIPLY:
            result *= equation[i + 1]
        elif operator == COMBINE:
            result = int(f"{result}{equation[i + 1]}")
    return result


def has_solution(equation: list[int], result: int) -> bool:
    if sum(equation) == result:
        return True
    # multiply all the numbers
    if math.prod(equation) == result:
        return True

    # Try all possible combinations of + and *
    operator_positions = len(equation) - 1
    for ops in product(["+", "*", "||"], repeat=operator_positions):
        if evaluate_expression(equation, ops) == result:
            return True

    return False


if __name__ == "__main__":
    sample_input = "dec_7/sample.input"
    real_input = "dec_7/real.input"
    lines = get_input(real_input)
    solutions_dict: dict[int, list[int]] = {}
    solved_dict: dict[int, bool] = {}

    for line in lines:
        equation, result = get_equation_and_result(line)
        solutions_dict[result] = equation

    for result, equation in solutions_dict.items():
        solved_dict[result] = has_solution(equation, result)

    solved_results = [result for result, solved in solved_dict.items() if solved]
    print(sum(solved_results))
