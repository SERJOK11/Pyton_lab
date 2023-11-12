import json


def task() -> float:
    with open('input.json') as file:
        data = json.load(file)

    result_sum = sum(entry["score"] * entry["weight"] for entry in data)

    return round(result_sum, 3)


print(task())
