"""
Chapter 13 exercises of "A Common-Sense Guide to Data Structures and Algorithms"
"""

def greatest_product_of_three_numbers(array):
    array.sort()
    return array[-1] * array[-2] * array[-3] 

def find_missing_number(array):
    array.sort()
    for i in range(len(array)):
        if array[i] + 1 != array[i+1]:
            return array[i] + 1
    return 0

def find_greatest_number_O_n_squared(array):
    for i in array:
        greatest = True
        for j in array:
            if j > i:
                greatest = False
        if greatest:
            return i
    return 0

def find_greatest_number_O_n_log_n(array):
    array.sort()
    return array[-1]

def find_greatest_number_O_n(array):
    greatest = 0
    for i in array:
        if i > greatest:
            greatest = i 
    return greatest


def main():
    print("Testing")
    int_array = [2,5,10,33,29,3,4,2,5,2,4,6,6,3,36,4,83]
    print(greatest_product_of_three_numbers(int_array))

    int_array = [9,3,2,5,6,7,1,0,4]
    print(find_missing_number(int_array))

    int_array = [2,5,10,33,29,3,4,2,5,2,4,6,6,3,36,4,83]
    print(find_greatest_number_O_n_squared(int_array))
    print(find_greatest_number_O_n_log_n(int_array))
    print(find_greatest_number_O_n(int_array))

main()