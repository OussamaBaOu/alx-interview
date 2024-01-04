#!/usr/bin/python3
"""
0. Pascal triangle
"""


def pascal_triangle(n):
    """Function def pascal_triangle(n): returns list of lists
    of integers representing Pascal’s triangle of n
    """
    r = []
    if n > 0:
        for i in range(1, n + 1):
            l = []
            a = 1
            for j in range(1, i + 1):
                l.append(a)
                a = a * (i - j) // j
            r.append(l)
    return r
