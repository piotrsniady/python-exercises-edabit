from math import factorial


def kempner(n: int) -> int:
    value = 1
    count = 0

    while True:
        if factorial(value) % n > 0:
            count += 1
        value += 1

        if factorial(value) % n == 0:
            count += 1
            break
    return count
