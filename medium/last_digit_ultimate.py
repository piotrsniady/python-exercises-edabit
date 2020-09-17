def last_dig(a: int, b: int, c: int) -> bool:
    last_a = [int(i) for i in str(a)][-1]
    last_b = [int(i) for i in str(b)][-1]
    last_c = [int(i) for i in str(c)][-1]

    if last_a * last_b == last_c:
        return True
    else:
        return False
