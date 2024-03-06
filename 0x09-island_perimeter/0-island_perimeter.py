#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculates perimeter of the island described in grid
    Args:
        grid: 2d list of integers containing 0 or 1
    Return:
        perimeter of the island
    """

    p = 0
    for a in range(len(grid)):
        for b in range(len(grid[i])):
            if (grid[a][b] == 1):
                if (a <= 0 or grid[a - 1][b] == 0):
                    p += 1
                if (a >= len(grid) - 1 or grid[a + 1][b] == 0):
                    p += 1
                if (b <= 0 or grid[a][b - 1] == 0):
                    p += 1
                if (b >= len(grid[a]) - 1 or grid[a][b + 1] == 0):
                    p += 1
    return p
