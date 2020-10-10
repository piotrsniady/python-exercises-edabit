def is_harshad(n: int) -> bool:
    sum_of_ciphers = sum([int(i) for i in str(n)])

    if n % sum_of_ciphers == 0:
        return True
    else:
        return False
