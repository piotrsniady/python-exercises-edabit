from typing import List


def loves_me(n: int) -> List[str]:
    lst = []
    for i in range(n):
        if i % 2 == 0:
            lst.append("Loves me")
        else:
            lst.append("Loves me not")

    lst[-1] = lst[-1].upper()

    return lst
