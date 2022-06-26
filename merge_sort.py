import math
import random


class Human:

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __str__(self):
        print(f'Hi! I`m {self.name}, {self.age} y.o. ')


def is_lower(potentially_lower, potentially_higher):
    if type(potentially_lower) is Human and type(potentially_higher) is Human:
        return potentially_lower.age - potentially_higher.age < 0
    return potentially_lower - potentially_higher > 0


def is_equal(number1, number2):
    if type(number1) is Human and type(number2) is Human:
        return number2.age == number1.age
    return number2 == number1


def is_base_two(n):
    a = math.log2(n)
    return int(a) == a


def divide_in_one_digit_parts(unsorted_list_sample):
    result_sequence = []

    if not is_base_two(len(unsorted_list_sample)):
        return None

    for element in unsorted_list_sample:
        result_sequence.append([element])
    return result_sequence


def merge(first_sequence, second_sequence):

    merged_sorted_sequence = []
    skip_indices = []
    first_sequence_index = 0
    second_sequence_index = 0

    while first_sequence_index < len(first_sequence) or second_sequence_index < len(second_sequence):

        while first_sequence_index in skip_indices:
            first_sequence_index += 1

        if first_sequence_index < len(first_sequence) and second_sequence_index < len(second_sequence):
            if is_lower(first_sequence[first_sequence_index], second_sequence[second_sequence_index]):
                merged_sorted_sequence.append(first_sequence[first_sequence_index])
                first_sequence_index += 1

            elif is_equal(first_sequence[first_sequence_index], second_sequence[second_sequence_index]):
                merged_sorted_sequence.append(first_sequence[first_sequence_index])
                first_sequence_index += 1

                if first_sequence[first_sequence_index-1] in first_sequence[first_sequence_index: len(first_sequence)]:
                    for i in range(first_sequence_index, len(first_sequence)):
                        if is_equal(first_sequence[first_sequence_index-1], first_sequence[i]):
                            skip_indices.append(i)
                            merged_sorted_sequence.append(first_sequence[i])

            elif not is_lower(first_sequence[first_sequence_index], second_sequence[second_sequence_index]):
                merged_sorted_sequence.append(second_sequence[second_sequence_index])
                second_sequence_index += 1

        elif first_sequence_index >= len(first_sequence):
            for element in second_sequence[second_sequence_index: len(second_sequence)]:
                merged_sorted_sequence.append(element)
                second_sequence_index += 1

        elif second_sequence_index >= len(second_sequence):
            for element in first_sequence[first_sequence_index: len(first_sequence)]:
                merged_sorted_sequence.append(element)
                first_sequence_index += 1

    return merged_sorted_sequence


def sort_using_merging(unsorted_list_sample):
    sorting_sequence = divide_in_one_digit_parts(unsorted_list_sample)
    number_of_merges = int(len(sorting_sequence)-1)
    current_merge_index = 1
    current_sequence_index = 0
    while number_of_merges >= current_merge_index:
        sorting_sequence.append(merge(sorting_sequence[current_sequence_index], sorting_sequence[current_sequence_index+1]))
        sorting_sequence = sorting_sequence[2: len(sorting_sequence)]
        current_merge_index += 1
    return sorting_sequence[len(sorting_sequence)-1]


unsorted_list_random = []
for i in range(256):
    unsorted_list_random.append(random.randint(2000, 694387))
print(sort_using_merging(unsorted_list_random))


human_unsorted_list = [Human('Bob', 13), Human('Kate', 13), Human('Steven', 45), Human('Alex', 88),Human('AK-47', 13), Human('Nata', 77), Human('Gay', 45), Human('Ilya', 88)]
for guy in sort_using_merging(human_unsorted_list):
    print(guy.name, guy.age)


