"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of 
candidates where the chosen numbers sum to target.

https://igotanoffer.com/blogs/tech/airbnb-software-engineer-interview
"""
from datetime import datetime


def target_sum(array, target):
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

def target_sum_backtracing():
    # https://www.geeksforgeeks.org/backtracking-introduction/
    # Enumeration Problem
    
    return 1


def main():
    start_time = datetime.now()
    target = 5
    array = [1, 2, 3, 4, 5, 6, 7, 10]

    result = target_sum(array, target)
    print(result)
    
    finish_time = datetime.now()
    print("Runtime: " + str(finish_time - start_time))

main()