"""
Assuming sorted arrays
"""

import math
from datetime import datetime
import random
import sys
sys.path.append('/Users/austin/workspace/CodingProblems/src/CodingProblems')
from test_data import arrays

def linear_search(arr, target):
    error = -1
    for i in range(len(arr)):
        if arr[i] == target:
            return target
    return error


def recursive_binary_search(arr, target):
    arr_length = len(arr)
    middle = math.floor(arr_length / 2)
    if arr[middle] != target and arr_length == 1:
        return -1
    elif arr[middle] == target:
        return target
    elif arr[middle] > target:
        left_arr = arr[:middle]
        return recursive_binary_search(left_arr, target)
    else:
        right_arr = arr[middle+1:]
        return recursive_binary_search(right_arr, target)
        

test_array_one = arrays.one_hundred_int_sequential_array
test_array_two = arrays.ten_thousand_int_sequential_array

target = random.randint(test_array_two[0], test_array_two[-1])

def main():
    print("Target: " + str(target) + "\n")
    start_time = datetime.now()
    print("Binary Search:")
    print(recursive_binary_search(test_array_two, target))
    finish_time = datetime.now()
    print("Runtime: " + str(finish_time - start_time))

    start_time = datetime.now()
    print("\nLinear Search:")
    print(linear_search(test_array_two, target))
    finish_time = datetime.now()
    print("Runtime: " + str(finish_time - start_time))

main()

