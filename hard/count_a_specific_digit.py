def digit_occurrences(start: int, end: int, n: int) -> int:
    num_count = 0

    for number in range(start, end + 1):
        if n in [int(j) for j in str(number)]:
            num_count += 1
    return num_count
