def convert_to_list(dictionary: dict) -> list:
    list_of_list = []

    for key, value in dictionary.items():
        list_of_list.append([f"{key}", value])

    return list_of_list
