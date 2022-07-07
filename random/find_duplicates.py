"""
Find duplicates in an array in the fastest possible algorithm
"""
import sys
from datetime import datetime
sys.path.append('/Users/austin/workspace/CodingProblems/src/CodingProblems')
from test_data import arrays

def find_duplicates_quadratic(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] == array[j]:
                return True
    return False

def find_duplicates_linear(array):
    duplicate_checker = {}
    for i in array:
        if get_key_value(duplicate_checker, array[i]) == 1:
            return True
        else:
            duplicate_checker[array[i]] = 1
    return False

def get_key_value(dict, key):
    try:
        return dict[key]
    except KeyError:
        return None

def main():
    test_array = arrays.ten_thousand_int_sequential_array_with_duplicate

    print("Test Quadratic Time")
    start_time = datetime.now()

    print(find_duplicates_quadratic(test_array))
    
    finish_time = datetime.now()
    print("Runtime: " + str(finish_time - start_time))

    print("Test Linear Time")
    start_time = datetime.now()

    print(find_duplicates_linear(test_array))
    
    finish_time = datetime.now()
    print("Runtime: " + str(finish_time - start_time))

main()
