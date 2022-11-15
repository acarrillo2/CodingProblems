"""
Chapter 1 Question 1.7: Rotate Matrix
"""

def rotate_matrix(matrix):
    new_matrix = create_empty_matrix(matrix)
    for rowIndex in range(len(matrix)):
        for columnIndex in range(len(matrix[0])):
            new_matrix[columnIndex][len(matrix)-1-rowIndex] = matrix[rowIndex][columnIndex]
    return new_matrix

def create_empty_matrix(matrix):
    new_matrix = []
    for row in matrix:
        blank_row = []
        new_matrix.append(blank_row)
        for column in row:
            blank_row.append(0)
    return new_matrix

def rotate_matrix_inplace(matrix):
    tempLeft = left
    right = top
    bottom = right
    left = bottom
    top = tempLeft
    return matrix

"""
layer1, it1
0,0 > 0,5
0,5 > 5,5
5,5 > 5,0
5,0 > 0,0

layer1, it2
0,1 > 1,5
1,5 > 5,4
5,4 > 4,0
4,0 > 0,1

layer2, it1
1,1 > 1,4
1,4 > 4,4
4,4 > 4,1
4,1 > 1,1

layer2, it2
1,2 > 2,4
2,4 > 4,3
4,3 > 3,1
3,1 > 1,2
"""




matrix = [
    [0,0,0,0,0,0],
    [0,1,0,0,0,0],
    [0,1,0,0,0,0],
    [0,1,0,0,0,0],
    [0,1,1,1,1,0],
    [0,0,0,0,0,0],
]

print("Before:")
for row in matrix:
    print(row)

new_matrix = rotate_matrix(matrix)

print("\nAfter:")
for row in new_matrix:
    print(row)


"""
Notes:

Round1:
0,0 > 0,5
0,1 > 1,5
0,2 > 2,5
0,3 > 3,5
0,4 > 4,5
0,5 > 5,5

Round2:
1,0 > 0,4
1,1 > 1,4
1,2 > 2,4
1,3 > 3,4
1,4 > 4,4
1,5 > 5,4

rowNew = columnOld
columnNew = len(row) - rowOld
"""