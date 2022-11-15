"""
Chapter 1 Question 1.8: Zero Matrix
"""

class Point:
    def __init__(self, row, column):
        self.row = row
        self.column = column


def zero_matrix(matrix):
    zero_list = []
    for rowIndex in range(len(matrix)):
        for columnIndex in range(len(matrix[0])):
            pointValue = matrix[rowIndex][columnIndex]
            if pointValue == 0:
                point = Point(rowIndex, columnIndex)
                zero_list.append(point)
    
    for point in zero_list:
        matrix = zero_out_cross(matrix, point)
    return matrix

def zero_out_cross(matrix, point):
    for i in range(len(matrix[point.row])):
        matrix[point.row][i] = 0
    for i in range(len(matrix)):
        matrix[i][point.column] = 0
    return matrix

def zero_matrix_no_point(matrix):
    rows_to_zero = []
    columns_to_zero = []
    for rowIndex in range(len(matrix)):
        for columnIndex in range(len(matrix[0])):
            pointValue = matrix[rowIndex][columnIndex]
            if pointValue == 0:
                rows_to_zero.append(rowIndex)
                columns_to_zero.append(columnIndex)
    
    for row in rows_to_zero:
        for column in range(len(matrix[0])):
            matrix[row][column] = 0
    for column in columns_to_zero:
        for row in range(len(matrix)):
            matrix[row][column] = 0
    return matrix

matrix = [
    [1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1],
    [1,1,1,1,1,1,1,0],
    [1,1,1,1,1,1,1,1],
    [1,1,1,0,1,1,1,1],
    [1,1,1,1,1,1,1,1],
]

print("Before:")
for row in matrix:
    print(row)

new_matrix = zero_matrix_no_point(matrix)

print("\nAfter:")
for row in new_matrix:
    print(row)

