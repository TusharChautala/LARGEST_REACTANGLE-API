# rectangle_solver.py

from typing import List

def largest_rectangle(matrix: List[List[int]]) -> tuple:
    if not matrix or not matrix[0]:
        return (0, 0)

    rows, cols = len(matrix), len(matrix[0])
    max_area = 0
    max_num = None

    for r in range(rows):
        for c in range(cols):
            num = matrix[r][c]
            width = 0
            for k in range(c, cols):
                if matrix[r][k] == num:
                    width += 1
                    area = width * (k - c + 1)
                    if area > max_area:
                        max_area = area
                        max_num = num
                else:
                    break

    print(f"Actual Result: {max_num, max_area}")  # Add this line to print the actual result
    return (max_num, max_area)
