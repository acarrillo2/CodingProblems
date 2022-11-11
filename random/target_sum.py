"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of 
candidates where the chosen numbers sum to target.

https://igotanoffer.com/blogs/tech/airbnb-software-engineer-interview
"""
from datetime import datetime


def target_sum_quadratic(array, target):
    result = []
    used_ints = []
    for i in array:
        for j in array:
            if i == j:
                pass
            elif i + j == target and i not in used_ints and j not in used_ints:
                result.append(str(i)+"+"+str(j))
                used_ints.append(i)
                used_ints.append(j)
    return result

def target_sum_map(array, target):
    match_dict = {}
    found_matches = []
    found_dict = {}
    for i in array:
        needed = target - i
        if i not in found_dict and needed in match_dict:
            found_matches.append(str(i) + "-" + str(needed))
            found_dict[i] = True
            found_dict[needed] = True
        match_dict[i] = True
    return found_matches


def target_sum_backtracing():
    # https://www.geeksforgeeks.org/backtracking-introduction/
    # Enumeration Problem
    
    return 1


def main():
    start_time = datetime.now()
    target = 5
    array = [1, 2, 3, 4, 5, 6, 7, 10, 7, 3]

    result = target_sum_quadratic(array, target)
    print(result)
    
    finish_time = datetime.now()
    print("Runtime: " + str(finish_time - start_time))

    print(target_sum_map(array, target))

main()