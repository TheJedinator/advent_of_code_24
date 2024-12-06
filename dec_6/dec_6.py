from collections import defaultdict
from enum import Enum


directions = {
    "UP": "^",
    "DOWN": "v",
    "LEFT": "<",
    "RIGHT": ">",
}


class TravelDirection(Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"


def find_current_position(
    map_list: list[str],
) -> tuple[tuple[int, int], TravelDirection] | tuple[None, None]:
    for i, row in enumerate(map_list):
        for j, cell in enumerate(row):
            if cell in directions.values():
                return ((i, j), TravelDirection(cell))
    return (None, None)


def find_trap_locations(map_list: list[str]) -> list[tuple[int, int]]:
    obstacles = find_obstacles(map_list)
    intersecting_obstacles = []
    obstacles_in_row = defaultdict(list[tuple[int, int]])
    obstacles_in_column = defaultdict(list[tuple[int, int]])
    print(obstacles)
    for obstacle in obstacles:
        x, y = obstacle
        obstacles_in_row[x].append(obstacle)
        obstacles_in_column[y].append(obstacle)
    for row, obstacles in obstacles_in_row.items():
        if len(obstacles) > 1:
            intersecting_obstacles.extend(obstacles)
    for column, obstacles in obstacles_in_column.items():
        if len(obstacles) > 1:
            intersecting_obstacles.extend(obstacles)

    return intersecting_obstacles


def find_obstacles(map_list: list[str]) -> list[tuple[int, int]]:
    obstacles: list[tuple[int, int]] = []
    for i, row in enumerate(map_list):
        for j, cell in enumerate(row):
            if cell == "#":
                obstacles.append((i, j))
    return obstacles


def get_map_string(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()


def get_map_list(file_path: str) -> list[str]:
    map_string = get_map_string(file_path)
    return map_string.split("\n")


def map_travel(map_list: list[str]) -> int:
    current_position, direction = find_current_position(map_list)
    assert direction is not None
    assert current_position is not None
    obstacles = find_obstacles(map_list)
    visited: set[tuple[int, int]] = set()
    visited.add(current_position)
    map_width, map_height = get_map_size(map_list)
    while (
        0 <= current_position[0] < map_width and 0 <= current_position[1] < map_height
    ):
        current_position = move_forward(current_position, direction)
        next_position = move_forward(current_position, direction)
        visited.add(current_position)
        if next_position in obstacles:
            direction = turn_right(direction)
        if (
            current_position[0] < 0
            or current_position[0] >= map_width
            or current_position[1] < 0
            or current_position[1] >= map_height
        ):
            break
    return len(visited) - 1


def find_path_intersections(map_list: list[str]) -> list[tuple[int, int]]:
    path_intersections: list[tuple[int, int]] = []
    obstacles = find_obstacles(map_list)
    for i, row in enumerate(map_list):
        for j, cell in enumerate(row):
            if cell == ".":
                if (i - 1, j) in obstacles and (i + 1, j) in obstacles:
                    if (i, j - 1) in obstacles and (i, j + 1) in obstacles:
                        path_intersections.append((i, j))
    return path_intersections


def get_map_size(map_list: list[str]) -> tuple[int, int]:
    return len(map_list), len(map_list[0])


def turn_right(direction: TravelDirection) -> TravelDirection:
    match direction:
        case TravelDirection.UP:
            return TravelDirection.RIGHT
        case TravelDirection.RIGHT:
            return TravelDirection.DOWN
        case TravelDirection.DOWN:
            return TravelDirection.LEFT
        case TravelDirection.LEFT:
            return TravelDirection.UP


def move_forward(
    current_position: tuple[int, int], direction: TravelDirection
) -> tuple[int, int]:
    x, y = current_position
    if direction == TravelDirection.UP:
        return (x - 1, y)
    elif direction == TravelDirection.DOWN:
        return (x + 1, y)
    elif direction == TravelDirection.LEFT:
        return (x, y - 1)
    elif direction == TravelDirection.RIGHT:
        return (x, y + 1)
    else:
        raise ValueError("Invalid direction")


if __name__ == "__main__":
    sample_input = "dec_6/sample.input"
    real_input = "dec_6/real.input"
    map_list = get_map_list(sample_input)
    print(map_travel(map_list))
    print(find_trap_locations(map_list))
