"""
Chapter 8 exercises of "A Common-Sense Guide to Data Structures and Algorithms"
"""


def find_intersection(arr1, arr2):
    arr1_index = {}
    intersection = []
    for i in arr1:
        arr1_index[i] = True
    for i in arr2:
        if safely_check_dict(arr1_index, i):
            intersection.append(i)
    return intersection

def find_first_duplicate(arr):
    dict = {}
    for i in arr:
        if safely_check_dict(dict, i):
            return i
        else:
            dict[i] = True
    return None

def find_missing_letter(phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alpha_dict = {}
    for c in alphabet:
        alpha_dict[c] = True
    for c in phrase:
        if safely_check_dict(alpha_dict, c):
            del alpha_dict[c]
    return list(alpha_dict.keys())[0]

def find_first_non_duplicate(word):
    letter_dict = {}
    for c in word:
        count = safely_check_dict(letter_dict, c)
        if count is None:
            count = 1
        else:
            count += 1
        letter_dict[c] = count
    print(letter_dict)
    for key in list(letter_dict.keys()):
        if letter_dict[key] == 1:
            return key


def test_question_one():
    print("Question 1")
    arr1 = [1,2,4,5,6,8]
    arr2 = [3,4,6,9,23]
    print(arr1)
    print(arr2)
    print("Intersection:")
    print(find_intersection(arr1, arr2))

def test_question_two():
    print("Question 2")
    arr = ["a", "b", "c", "d", "c", "a"]
    print(arr)
    print("First Duplicate:")
    print(find_first_duplicate(arr))

def test_question_three():
    print("Question 3")
    phrase = "the quick brown box jumps over a lazy dog"
    print(phrase)
    print("Missing letter:")
    print(find_missing_letter(phrase))

def test_question_four():
    print("Question 4")
    word = "minimum"
    print(word)
    print("First non-duplicate in String:")
    print(find_first_non_duplicate(word))   

def safely_check_dict(dict, key):
    try:
        return dict[key]
    except KeyError:
        return None

def main():
    test_question_one()
    test_question_two()
    test_question_three()
    test_question_four()

main()