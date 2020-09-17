def stupid_addition(a: [int, str], b: [int, str]) -> [str, int, None]:
    if isinstance(a, int) and isinstance(b, int):
        return f"{a}{b}"
    elif isinstance(a, str) and isinstance(b, str):
        return int(a) + int(b)
    else:
        return None
