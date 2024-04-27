#!/usr/bin/python3
"""0-pascal_triangle"""


def pascal_triangle(n):
    """Get a list of lists of intergers 
    representing the pascal's triangle
    """
    triangle = []
    if n <= 0:
        return triangle
    else:
        for row in range(n):
            if row == 0:
                triangle.append([1])
            elif row == 1:
                triangle.append([1, 1])
            else:
                next_row = [1]
                prev_row = triangle[-1]
                for i in range(len(prev_row)-1):
                    next_row.append(prev_row[i] + prev_row[i+1])
                next_row.append(1)
                triangle.append(next_row)
        return triangle
