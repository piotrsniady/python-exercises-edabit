def harmonic(num: int):
    harmonic_func = 0

    for i in range(1, num + 1):
        harmonic_func += 1 / i
    return harmonic_func
