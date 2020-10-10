import re


def get_char(string, char):
    return re.findall(pattern=fr'.?\d+(?={char})', string=string)[0]


def process_sign(value):
    if value[0] == "+":
        value.replace("+", "")
        return int(value)
    else:
        return int(value)


def solve(equation: str) -> float:
    a = get_char(string=equation, char="x")
    b = get_char(string=equation, char="=")
    y = int(equation.split("=")[1])

    a = process_sign(value=a)
    b = process_sign(value=b)

    x = (y - b) / a
    return x


res = solve(equation="2x+1=4")
print(res)
