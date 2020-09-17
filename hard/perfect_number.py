def check_perfect(n: int) -> bool:
    sum_of_factors = sum([fact_num for fact_num in range(1, n) if n % fact_num == 0])

    if sum_of_factors == n:
        return True
    else:
        return False
