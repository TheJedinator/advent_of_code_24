from left_list import left_list
from right_list import right_list
from copy import deepcopy
from rich import print

left_copy = deepcopy(left_list)
right_copy = deepcopy(right_list)
sorted_left = sorted(left_copy)
sorted_right = sorted(right_copy)

print(f"Sorted Left list has {len(sorted_left)} elements")
print(f"Sorted Right list has {len(sorted_right)} elements")


def distance_between_elements(element1: int, element2: int) -> int:
    # find the larger element
    if element1 > element2:
        larger = element1
        smaller = element2
    else:
        larger = element2
        smaller = element1
    # print(f"Distance between {element1} and {element2} is {larger - smaller}")
    return larger - smaller


def get_total_distance():
    distances = []
    for i in range(len(sorted_left)):
        distances.append(distance_between_elements(sorted_left[i], sorted_right[i]))

    distance_total = sum(distances)
    print(f"Total distance: {distance_total}")


similarity_score_total = 0


def calculate_similarity_score(number: int):
    number_of_occurences = sorted_right.count(number)
    similarity_score = number * number_of_occurences
    return similarity_score


def get_total_similarity_score():
    similarity_scores = []
    for i in range(len(sorted_left)):
        similarity_scores.append(calculate_similarity_score(sorted_left[i]))

    similarity_score_total = sum(similarity_scores)
    print(f"Total similarity score: {similarity_score_total}")


if __name__ == "__main__":
    # get_total_distance()
    get_total_similarity_score()
