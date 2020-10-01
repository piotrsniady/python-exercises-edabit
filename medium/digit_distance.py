def digit_distance(n1: int, n2: int) -> int:
    return sum([abs(int(i[0]) - int(i[1])) for i in list(zip(str(n1), str(n2)))])
