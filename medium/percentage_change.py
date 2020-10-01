def percentage_change(a: str, b: str) -> str:
    num_a = int(a.replace("$", ""))
    num_b = int(b.replace("$", ""))
    value = int(((num_a - num_b) / num_a) * 100)

    if num_a < num_b:
        return f"{value}% increase"
    else:
        return f"{value}% decrease"
