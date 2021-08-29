"""
Assuming sorted arrays
"""

import math
from datetime import datetime
import random
import sys
sys.path.append('/Users/austin/workspace/CodingProblems/src/CodingProblems')
from test_data.arrays import ten_thousand_int_array

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
        

test_array_one = [1,2,3,4,5,7,8]
test_array_two = [10,5,6,28,4,60,43,6,3,4,4,2,1,3]
test_array_three = [1]
test_array_four = [1,4,10]
test_array_five = []
test_array_six = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,6,7,7,8,8,9,9,11,10,13,13,13,14,15,16,62,73,1515,111,54,76,123,23424,453,363,252,26,63,1,1,1,12,3,3,4,4,5,5,56,5,3,3,33]

test_array_seven = ten_thousand_int_array

target = random.randint(test_array_seven[0], test_array_seven[-1])

def main():
    print("Target: " + str(target) + "\n")
    start_time = datetime.now()
    print("Binary Search:")
    print(recursive_binary_search(test_array_seven, target))
    finish_time = datetime.now()
    print("Runtime: " + str(finish_time - start_time))

    start_time = datetime.now()
    print("\nLinear Search:")
    print(linear_search(test_array_seven, target))
    finish_time = datetime.now()
    print("Runtime: " + str(finish_time - start_time))

main()

