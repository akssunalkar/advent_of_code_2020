import numpy as np
import math


def get_seat_id(row, col):
    return (row * 8) + col


all_boarding_ids = open("problem5.txt", "r").readlines()


def get_row(seat_string):
    low_row = 0
    high_row = 127
    row = seat_string[:7]
    for r in row:
        if r == "F":
            high_row = math.floor(np.median(np.arange(low_row, high_row + 1)))
        elif r == "B":
            low_row = math.ceil(np.median(np.arange(low_row, high_row + 1)))
    assert low_row == high_row
    final_row = int(low_row)
    return final_row


def get_col(seat_string):
    low_col = 0
    high_col = 7
    col = seat_string[7:]
    for c in col:
        if c == "R":
            low_col = math.ceil(np.median(np.arange(low_col, high_col + 1)))
        elif c == "L":
            high_col = math.floor(np.median(np.arange(low_col, high_col + 1)))

    assert low_col == high_col
    final_col = int(low_col)
    return final_col


def get_all_seat_id():
    seat_id_list = []
    for i, bpass in enumerate(all_boarding_ids):
        final_row, final_col = get_row(bpass), get_col(bpass)
        s_id = get_seat_id(final_row, final_col)
        seat_id_list.append(s_id)

    return seat_id_list


all_seat_ids = get_all_seat_id()
# Part1
max_seat_id = max(all_seat_ids)
print(max_seat_id)

# Part2
first_seat_id, last_seat_id = sorted(all_seat_ids)[0], sorted(all_seat_ids)[-1]
ideal_range = set(list(range(first, last + 1)))
missing_seat_id = ideal_range.difference(set(all_seat_ids))
print(missing_seat_id)
