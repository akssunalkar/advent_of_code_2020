import os
from tqdm.auto import tqdm
import numpy as np

text = open("problem1.txt", "r").readlines()
number_list = sorted([int(t) for t in tqdm(text)])

target_value = 2020


def twosum(nums, target):
    low = 0
    high = len(nums) - 1
    while low < high:
        addition = nums[low] + nums[high]

        if addition == target:
            return nums[low], nums[high]

        elif addition > target:
            high -= 1
        else:
            low += 1


def threesum(num_list, t):
    for i in range(len(num_list)):
        new_target = target_value - num_list[i]
        result = twosum(num_list[i:], new_target)
        if result:
            return (num_list[i], *result)


# for i in range(len(number_list)):
# 	for j in range(i, len(number_list)):
# 		for k in range(j, len(number_list)):
# 			if number_list[i] + number_list[j] + number_list[k] == target_value:
# 				print(number_list[i], number_list[j], number_list[k])
# 				break

a, b, c = threesum(number_list, 2020)
print(a, b, c)
print(a * b * c)
