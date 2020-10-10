def is_heteromecic(n: int) -> bool:
    for i in range(1, n + 1):
        if i * (i + 1) == n:
            return True
        else:
            return False
