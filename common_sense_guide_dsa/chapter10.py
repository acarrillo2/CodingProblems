"""
Chapter 10 exercises of "A Common-Sense Guide to Data Structures and Algorithms"
"""
test_array = [1, 2, 3,
        [4, 5, 6],
        7,
        [8,
            [9, 10, 11,
                [12, 13, 14]
            ]
        ], [15, 16, 17, 18, 19,
                [20, 21, 22,
                    [23, 24, 25,
                        [26, 27, 29]
                    ],
                 30, 31],
            32],
         3]

def print_list(array):
    for i in array:
        if isinstance(i, int):
            print(i)
        else:
            print_list(i)


def main():
    print("Testing")
    print_list(test_array)

main()