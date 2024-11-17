def connect_dicts(dict1: dict, dict2: dict) -> dict:

    if sum(dict1.values()) > sum(dict2.values()):
        dict3 = {**dict2, **dict1}
    else:
        dict3 = {**dict1, **dict2}

    key_to_remove = [key for key, value in dict3.items() if value < 10]

    for key in key_to_remove:
        dict3.pop(key)

    return dict(sorted(dict3.items(), key=lambda item: item[1]))


print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))