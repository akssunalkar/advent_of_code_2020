from collections import Counter
import numpy as np


text = open("problem6.txt", "r").readlines()


def get_qs_ans(sample):
    s_list = []
    x = y = 0
    temp = []
    while y < len(sample):
        ch = sample[y].rstrip("\n")
        if y != len(sample) - 1:
            if sample[y + 1][0] == "\n":
                temp.append(ch)
                s_list.append(temp)
                temp = []
                y += 2
            else:
                temp.append(ch)
                y += 1
        else:
            s_list.append(temp + [ch])
            break

    return s_list


list_qs = get_qs_ans(text)

# Part 1
def get_count_of_yes(list_of_qs):
    num_count = 0
    for s in list_of_qs:
        qs = "".join(s)

        num_count += len(Counter(list(qs)))
    return num_count


count = get_count_of_yes(list_qs)

# Part 2
def get_count_of_all_yes(list_of_qs):
    n = 0
    for s in list_of_qs:
        list_of_sets = list(map(set, list(s)))
        common_qs = set.intersection(*list_of_sets)
        n += len(common_qs)
    return n


all_yes_count = get_count_of_all_yes(list_qs)

