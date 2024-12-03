import re
from rich import print


def get_input_string() -> str:
    with open(
        "/Users/jedp/personal_github/advent_of_code_24/dec_3/dec_3.input", "r"
    ) as file:
        return file.read()


def find_mul_commands_from_input(input_str: str) -> list[tuple[int, int]]:
    pattern = r"mul\((\d{1,3},\d{1,3})\)"
    matches = re.findall(pattern, input_str)
    int_matches = []
    for match in matches:
        int_pair = match.split(",")
        int_tuple = (int(int_pair[0]), int(int_pair[1]))
        int_matches.append(int_tuple)
    return int_matches


def get_executable_commands(input_str: str) -> list[str]:
    dont_pattern = re.compile("(do?n't)")
    do_pattern = re.compile("do(?!n)")
    to_do = do_pattern.split(input_str)
    real_dos = []
    for todo in to_do:
        real_dos.append(re.split(dont_pattern, todo)[0])
    return real_dos


def multiply_match(match: tuple[int, int]) -> int:
    return match[0] * match[1]


def execute_part_1(input_str: str) -> int:
    matches = find_mul_commands_from_input(input_str)
    products = [multiply_match(match) for match in matches]
    return sum(products)


def execute_part_2(input_str: str) -> int:
    executable_commands = [c for c in get_executable_commands(input_str)]
    all_products = []
    for command in executable_commands:
        matches = find_mul_commands_from_input(command)
        products = [multiply_match(match) for match in matches]
        all_products.extend(products)
    return sum(all_products)


if __name__ == "__main__":
    print(execute_part_1(get_input_string()))
    print(execute_part_2(get_input_string()))
