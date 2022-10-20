import math
import matplotlib.pyplot as plt

from Table import Table


def get_frequency_table(data):
    table = Table(column_names=["number_of_views", "number_of_occurrences"])
    for number_of_views in data:
        if number_of_views not in table["number_of_views"]:
            table.append({"number_of_views": number_of_views, "number_of_occurrences": 1})
        else:
            table.find_row_by_value(number_of_views, "number_of_views")["number_of_occurrences"] += 1

    return table


def get_cumulative_frequency_table(data):
    data = sorted(data)
    table = Table(column_names=["number_of_views", "number_of_occurrences"])
    for number_of_views in data:
        if number_of_views not in table["number_of_views"]:
            previous_value = table[-1]["number_of_occurrences"] if len(table) else 0
            table.append({"number_of_views": number_of_views,
                          "number_of_occurrences": 1 + previous_value})
        else:
            table.find_row_by_value(number_of_views, "number_of_views")["number_of_occurrences"] += 1

    return table


def task1(data):
    frequency_table = get_frequency_table(data)
    frequency_table.save_as("output/frequency_table.txt")

    cumulative_frequency_table = get_cumulative_frequency_table(data)
    cumulative_frequency_table.save_as("output/cumulative_frequency_table.txt")

    max_number_of_views = max(data)
    with open("output/other.txt", 'w') as file:
        file.write(f"Max number of views is {max_number_of_views} and "
                   f"the movie number is {data.index(max_number_of_views) + 1}\n")


def task2(data):
    frequency_table = get_frequency_table(data)

    mode = frequency_table.find_row_by_value(max(frequency_table['number_of_occurrences']),
                                             'number_of_occurrences')["number_of_views"]
    with open("output/other.txt", 'a') as file:
        file.write(f"The mode is {mode}\n")

    data = sorted(data)
    if len(data) % 2 != 0:
        median = data[math.floor(len(data) / 2)]
    else:
        mid_indeces = (len(data) / 2 - 1, len(data) / 2)
        median = (data[int(mid_indeces[0])] + data[int(mid_indeces[1])]) / 2
    with open("output/other.txt", 'a') as file:
        file.write(f"The median is {median}\n")


def task3(data):
    mean = sum(data) / len(data)
    variance = sum([(i - mean) ** 2 for i in data]) / (len(data))
    with open("output/other.txt", 'a') as file:
        file.write(f"The variance is {variance}\n")

    with open("output/other.txt", 'a') as file:
        file.write(f"The standard deviation is {math.sqrt(variance)}\n")


def task4(data):
    plt.bar(x=range(len(data)), height=data)
    plt.ylabel('Number of views')
    plt.xlabel('Movie ID')
    plt.savefig('output/plot.png', bbox_inches='tight')


def read_file(filename):
    with open(filename) as file:
        lines = file.readlines()

    data = []
    for line in lines:
        data.append(int(line.strip()))

    return data


def main():
    print("Рябиця Максим Андрійович\n"
          "ІПЗ-21(2)\n")

    filename = input("Enter filename: ")
    data = read_file(filename)
    data.pop(0)

    while True:
        print("\n1. Task 1\n"
              "2. Task 2\n"
              "3. Task 3\n"
              "4. Task 4\n"
              "0. Exit\n")

        task_number = int(input("Enter task number: "))
        match task_number:
            case 1:
                task1(data)
            case 2:
                task2(data)
            case 3:
                task3(data)
            case 4:
                task4(data)
            case 0:
                break


if __name__ == "__main__":
    main()
