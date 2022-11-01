"""
Chapter 19 exercises of "A Common-Sense Guide to Data Structures and Algorithms"
"""

def reverse(array):
    length = len(array)
    for i in range(length // 2):
        temp = array[i]
        array[i] = array[length - 1 - i]
        array[length - 1 - i] = temp
    return array

def main():
    print("Testing")
    test_array = [1,2,3,4,5,6,7,8,9,10]
    print(reverse(test_array))

main()