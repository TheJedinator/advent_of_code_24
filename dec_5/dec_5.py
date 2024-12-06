from collections import deque


def get_priorities(input: str) -> list[tuple[int, int]]:
    return [
        (int(a), int(b))
        for a, b in (line.split("|") for line in input.strip().splitlines())
    ]


def get_print_jobs(input: str) -> list[list[int]]:
    jobs = [[int(p) for p in line.split(",")] for line in input.strip().splitlines()]
    return jobs


def get_priorities_related_to_job(
    job: list[int], priorities: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    return [p for p in priorities if p[0] in job and p[1] in job]


def sort_job_by_priorities(
    job: list[int], priorities: list[tuple[int, int]]
) -> tuple[list[int], bool]:
    # Create a graph representation
    graph: dict[int, list[int]] = {x: [] for x in job}
    dependency_count = {x: 0 for x in job}

    for before, after in priorities:
        if before in job and after in job:
            graph[before].append(after)
            dependency_count[after] += 1

    # TIL: Deque is like a double linked list
    queue = deque([page for page in job if dependency_count[page] == 0])
    sorted_job: list[int] = []

    while queue:
        # Exhaust the queue and extract the page - we can already print it because
        # there are no depencies
        page = queue.popleft()
        sorted_job.append(page)
        for neighbor in graph[page]:
            # Look at the edges for this page and decrement the dependency count
            dependency_count[neighbor] -= 1
            # If the dependency count is zero, we can print this page
            if dependency_count[neighbor] == 0:
                queue.append(neighbor)

    modified = sorted_job != job
    return sorted_job, modified


def sort_all_jobs(
    jobs: list[list[int]], priorities: list[tuple[int, int]]
) -> tuple[list[list[int]], list[list[int]]]:
    modified_jobs: list[list[int]] = []
    unmodified_jobs: list[list[int]] = []

    for job in jobs:
        sorted_job, modified = sort_job_by_priorities(job, priorities)
        if modified:
            print(f"Modified job: {sorted_job}")
            modified_jobs.append(sorted_job)
        else:
            print(f"Unmodified job: {sorted_job}")
            unmodified_jobs.append(sorted_job)
    return unmodified_jobs, modified_jobs


def get_middle_page_number_of_job(job: list[int]) -> int:
    return job[len(job) // 2]


def solve(priority_string: str, jobs_string: str) -> tuple[int, int]:
    priorities = get_priorities(priority_string)
    jobs = get_print_jobs(jobs_string)
    unmodified_jobs, modified_jobs = sort_all_jobs(jobs, priorities)
    unmodified_sum = sum(get_middle_page_number_of_job(job) for job in unmodified_jobs)
    modified_sum = sum(get_middle_page_number_of_job(job) for job in modified_jobs)
    return unmodified_sum, modified_sum


if __name__ == "__main__":
    jobs_string = open("jobs.input", "r").read()
    priority_string = open("priorities.input", "r").read()

    print(solve(priority_string, jobs_string))
