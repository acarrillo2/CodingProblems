"""
Chapter 11 exercises of "A Common-Sense Guide to Data Structures and Algorithms"
"""

def count_characters_in_array(array):
    length_of_first_item_in_array = len(array[0])
    if (len(array) == 1):
        return length_of_first_item_in_array
    return length_of_first_item_in_array + count_characters_in_array(array[1:])

def return_even_numbers(array, i):
    if len(array) - 1 == i:
        return array
    if array[i] % 2 == 0:
        return return_even_numbers(array, i + 1)
    else:
        array = array[:i] + array[i+1:]
        return return_even_numbers(array, i)

def return_even_numbers_one_arg(array):
    if len(array) == 1:
        if array[0] % 2 == 0:
            return array
        else: 
            return []
    if array[0] % 2 == 0:
        return [array[0]] + return_even_numbers_one_arg(array[1:])
    else:
        return return_even_numbers_one_arg(array[1:])

def triangle_numbers(n):
    if n == 1:
        return n
    return n + triangle_numbers(n-1)

def find_first_x_at_least_one_x(string):
    if string[0] == "x":
        return 0
    return 1 + find_first_x_at_least_one_x(string[1:])

def shortest_paths(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return shortest_paths(rows - 1, columns) + shortest_paths(rows, columns - 1)


def main():
    print("Testing")
    test_array = ["ab", "c", "def", "ghij"]
    print(count_characters_in_array(test_array))

    test_array = [1, 2, 3, 4, 5, 7, 10]
    print(return_even_numbers_one_arg(test_array))

    print(triangle_numbers(7))

    string = "abcdefghijklmnopqrstuvwxyz"
    print(find_first_x_at_least_one_x(string))

    print(shortest_paths(3, 7))
    

main()