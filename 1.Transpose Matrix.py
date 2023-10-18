"""
Transpose Matrix Problem
In the Transpose Matrix problem, we need to manipulate a matrix by reversing its rows and columns.\
    This problem is commonly used in computer science and mathematics and has many applications in areas \
    such as image processing, linear algebra, and graph theory.

Here’s an example of the input and output values of this problem:

Input: [[1,2,3],[4,5,6],[7,8,9]] | Output: [[1,4,7],[2,5,8],[3,6,9]]
The dimensions of a matrix are n x m, where n is the number of rows and m is the number of columns.\
    After transposing a matrix, the dimensions are reversed into an m x n matrix.
"""


def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])

    transposed = [[0 for j in range(n)] for i in range(m)]

    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]
    return transposed


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(matrix))
