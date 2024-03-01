#!/usr/bin/python3
"""
Function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    This function that multiplies 2 matrices
    m_a and m_b must be list of lists (int or float)
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")

    if m_a in ([], [[]]):
        raise ValueError("m_a can't be empty")
    if m_b in ([], [[]]):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for index in row:
            if not isinstance(index, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for index in row:
            if not isinstance(index, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    len_col_a = len(m_a[0])
    for row in m_a:
        if len(row) != len_col_a:
            raise TypeError("each row of m_a must be of the same size")

    total_m_b = len(m_b[0])
    for row in m_b:
        if len(row) != total_m_b:
            raise TypeError("each row of m_b must be of the same size")

    len_row_b = len(m_b)

    if len_col_a != len_row_b:
        raise ValueError("m_a and m_b can't be multiplied")

    matrix = [[0 for i in range(total_m_b)] for j in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                matrix[i][j] += (m_a[i][k] * m_b[k][j])

    return matrix
