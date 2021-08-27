"""
Given an array n integers, are there elements a, b, c in array such that sum of (a,b,c) equals to a particular target X?

How can you solve this same problem if you want unique triplets?
"""
from datetime import datetime, timedelta

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

test_array_one = [1,2,3,4,5,7,8]
test_array_two = [10,5,6,28,4,60,43,6,3,4,4,2,1,3]
test_array_three = [1]
test_array_four = [1,4,10]
test_array_five = []
test_array_six = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,6,7,7,8,8,9,9,11,10,13,13,13,14,15,16,62,73,1515,111,54,76,123,23424,453,363,252,26,63,1,1,1,12,3,3,4,4,5,5,56,5,3,3,33]


target = 15

def main():
    start_time = datetime.now()
    answer = unique_triplets(test_array_six, target)
    render_arrays(answer)
    finish_time = datetime.now()
    print("Runtime: " + str(finish_time - start_time))

main()