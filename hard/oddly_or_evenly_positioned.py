from typing import List


def char_at_pos(num_list: list, opt: str) -> List[int]:
    positions = []
    for index, value in enumerate(num_list):
        if opt == "even":
            if (index + 1) % 2 == 0:
                positions.append(value)
        elif opt == "odd":
            if (index + 1) % 2 != 0:
                positions.append(value)
    return positions
