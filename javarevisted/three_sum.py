"""
Given an array n integers, are there elements a, b, c in array such that sum of (a,b,c) equals to a particular target X?

How can you solve this same problem if you want unique triplets?
"""
from datetime import datetime
import sys
sys.path.append('/Users/austin/workspace/CodingProblems/src/CodingProblems')
from test_data import arrays

def triplets(arr, target):
    arr.sort()
    results = []
    for i in range(len(arr)-2):
        l = i + 1
        r = len(arr) - 1
        while l < r:
            sum = arr[l] + arr[i] + arr[r]
            if sum == target:
                triplet = [arr[l], arr[i], arr[r]]
                results.append(triplet)
                l += 1
                r -= 1
            elif sum > target:
                r -= 1
            else:
                l += 1
    return results

def unique_triplets(arr, target):
    arrays = triplets(arr, target)
    results = []
    for arr in arrays:
        arr.sort()
        arr_string = str(arr[0]) + ":" + str(arr[1]) + ":" + str(arr[2])
        if arr_string not in results:
            results.append(arr_string)
    return results


def render_arrays(arrays):
    for arr in arrays:
        print(arr)

test_array_one = arrays.one_hundred_int_sequential_array
test_array_two = arrays.one_hundred_int_random_array
test_array_three = arrays.ten_thousand_int_sequential_array

target = 15

def main():
    start_time = datetime.now()
    answer = unique_triplets(test_array_one, target)
    render_arrays(answer)
    finish_time = datetime.now()
    print("Runtime: " + str(finish_time - start_time))

main()