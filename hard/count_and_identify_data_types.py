from typing import Any


def count_datatypes(*args: Any) -> list:
    types_dict = {int: 0, str: 0, bool: 0, list:0, tuple:0, dict: 0}

    if len(args) > 0:
        for arg in args:
            for key, value in types_dict.items():
                if type(arg) == key:
                    types_dict[key] += 1
        return list(types_dict.values())
    else:
        return list(types_dict.values())
