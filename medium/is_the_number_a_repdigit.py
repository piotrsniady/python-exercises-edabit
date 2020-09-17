def is_repdigit(num: int) -> bool:
    if num < 0:
        return False
    else:
        numbers = [int(digit) for digit in str(num)]
        if numbers[1:] == numbers[:-1] or num == 0:
            return True
