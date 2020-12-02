import os
from tqdm.auto import tqdm
from collections import Counter
import numpy as np

text = open("problem2.txt", "r").readlines()


def process_line(l):
    split_line = l.rstrip("\n").split(" ")
    policy, letter, pwd = (
        list(map(int, split_line[0].split("-"))),
        split_line[1].rstrip(":"),
        split_line[2],
    )
    return policy, letter, pwd


## Part1
def policy1():
    count = 0
    for idx, line in enumerate(tqdm(text)):
        policy, letter, pwd = process_line(line)
        char_count = Counter(pwd)
        if letter in char_count and policy[0] <= char_count[letter] <= policy[1]:
            count += 1

    return count


## part2
def policy2():
    count = 0
    for idx, line in enumerate(tqdm(text)):
        policy, letter, pwd = process_line(line)

        if pwd[policy[0] - 1] == letter and pwd[policy[1] - 1] == letter:
            continue
        if pwd[policy[0] - 1] != letter and pwd[policy[1] - 1] != letter:
            continue
        else:
            print(policy, letter, pwd)
            count += 1
    return count


valid_count = policy2()
