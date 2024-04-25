#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """Generate a list of lists of intergers representing the pascal's triangle

Args:
    n (int): the number of rows in the triangle

Return:
    triangle (list): a list of list representing Pascal triangle
    """
    if n <= 0:
        return []
    else:
        triangle = []
        for row in range(n):
            if row == 0:
                triangle.append([1])
            elif row == 1:
                triangle.append([1,1])
            else:
                next_row = [1]
                prev_row = triangle[-1]
                for i in range(len(prev_row)-1):
                    next_row.append(prev_row[i] + prev_row[i+1])
                next_row.append(1)
                triangle.append(next_row)
        return triangle

