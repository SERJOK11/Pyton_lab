import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:

    with open(INPUT_FILENAME, newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        data_list = []

        for row in csv_reader:

            data_list.append(row)

    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(data_list, json_file, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
