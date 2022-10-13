"""
Chapter 12 exercises of "A Common-Sense Guide to Data Structures and Algorithms"
"""
from datetime import datetime



def add_until_100(array):
    if len(array) == 0:
        return 0
    if array[0] + add_until_100(array[1:]) > 100:
        return add_until_100(array[1:])
    else:
        return array[0] + add_until_100(array[1:])

def add_until_100_single_call(array):
    if len(array) == 0:
        return 0
    remainder = add_until_100_single_call(array[1:])
    if array[0] + remainder > 100:
        return remainder
    else:
        return array[0] + remainder

def golomb(n):
    if n == 1:
        return 1
    return 1 + golomb(n - golomb(golomb(n - 1)))

def golomb_memoization(n, map):
    if n == 1:
        return 1
    if n in map:
        return map[n]
    golomb_value = 1 + golomb_memoization(n - golomb_memoization(golomb_memoization(n - 1, map), map), map)
    map[n] = golomb_value
    return golomb_value

def shortest_paths(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return shortest_paths(rows - 1, columns) + shortest_paths(rows, columns - 1)

def shortest_paths_improved(rows, columns, map):
    if rows == 1 or columns == 1:
        return 1
    key1 = str(rows - 1) + ":" + str(columns)
    key2 = str(rows) + ":" + str(columns - 1)
    value1 = 0
    value2 = 0
    if key1 in map:
        value1 = map[key1]
    else:
        value1 = shortest_paths_improved(rows - 1, columns, map)
        map[key1] = value1
    if key2 in map:
        value2 = map[key2] 
    else:
        value2 = shortest_paths_improved(rows, columns - 1, map)
        map[key2] = value2
    
    return value1 + value2

def main():
    print("Testing")
    number_array = [1,2,6,5,10,2,3,5,2,5,23,2,23,3,2,1,5,3]
    start_time = datetime.now()
    print(add_until_100(number_array))
    finish_time = datetime.now()
    print("Runtime add_until_100: " + str(finish_time - start_time))
    
    start_time = datetime.now()
    print(add_until_100_single_call(number_array))
    finish_time = datetime.now()
    print("Runtime add_until_100_single_call: " + str(finish_time - start_time))


    start_time = datetime.now()
    print(golomb(23))
    finish_time = datetime.now()
    print("Runtime golomb: " + str(finish_time - start_time))

    start_time = datetime.now()
    print(golomb_memoization(23, {}))
    finish_time = datetime.now()
    print("Runtime golomb_memoization: " + str(finish_time - start_time))



    start_time = datetime.now()
    print(shortest_paths(10, 10))
    finish_time = datetime.now()
    print("Runtime shortest_paths: " + str(finish_time - start_time))

    start_time = datetime.now()
    print(shortest_paths_improved(10, 10, {}))
    finish_time = datetime.now()
    print("Runtime shortest_paths_improved: " + str(finish_time - start_time))

main()