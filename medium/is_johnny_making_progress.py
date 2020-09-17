from typing import List


def progress_days(num_list: list) -> List[tuple]:
    return [(x, y) for x, y in (zip(num_list, num_list[1:])) if x < y]
