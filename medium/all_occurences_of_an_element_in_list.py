from typing import List


def got_indices(lst: list, char: str) -> List[int]:
    return [ind for ind, val in enumerate(lst) if val == char]
