from tqdm.auto import tqdm
import json
import numpy as np

batch_files = open("problem4.txt", "r").readlines()

passport_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])
optional = "cid"


def get_all_ids():
    all_ids = []
    ids = []
    flag = False
    for i, line in enumerate(batch_files):
        if i == len(batch_files) - 1:
            ids = [line.rstrip("\n")]
            format_list = " ".join(ids)
            map_format = dict(item.split(":") for item in format_list.split(" "))
            all_ids.append(map_format)
        if line[0] == "\n":
            flag = True
            format_list = " ".join(ids)
            map_format = dict(item.split(":") for item in format_list.split(" "))
            all_ids.append(map_format)
            ids = []
            continue
        ids.append(line.rstrip("\n"))

    return all_ids


def check_valid(passport):
    keys_in_passport = set(passport.keys())
    find_missing = passport_fields.difference(keys_in_passport)
    if optional in find_missing:
        find_missing.remove(optional)
    if len(find_missing) >= 1:
        return False
    return True


def get_valid_count(list_passport_ids):
    valid_count = 0
    for idx, p in enumerate(list_passport_ids):
        if check_valid(p):
            valid_count += 1
    return valid_count


def check_fields(passport):
    if check_valid(passport):

        flag_array = [False] * 7

        if 1920 <= int(passport["byr"]) <= 2002:
            flag_array[0] = True

        if 2010 <= int(passport["iyr"]) <= 2020:
            flag_array[1] = True

        if 2020 <= int(passport["eyr"]) <= 2030:
            flag_array[2] = True

        if "cm" in passport["hgt"]:
            if 150 <= int(passport["hgt"].split("cm")[0]) <= 193:
                flag_array[3] = True

        if "in" in passport["hgt"]:
            if 59 <= int(passport["hgt"].split("in")[0]) <= 76:
                flag_array[3] = True

        if "#" in passport["hcl"] and len(passport["hcl"]) == 7:
            char_allowed = set(list("0123456789abcdef"))
            char_in_hcl = set(list(passport["hcl"][1:]))

            if len(char_in_hcl.difference(char_allowed)) == 0:
                flag_array[4] = True

        if passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            flag_array[5] = True

        if len(passport["pid"]) == 9 and passport["pid"].isdigit():
            flag_array[6] = True

        if np.all(flag_array):
            return True
    return False


all_passport_ids = get_all_ids()

# Part1
num_valid = get_valid_count(all_passport_ids)
print(num_valid)

# Part2
field_and_key_valid_count = 0
for i, p in enumerate(all_passport_ids):
    if check_fields(p):
        field_and_key_valid_count += 1

print(field_and_key_valid_count)
