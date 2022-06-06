#!/usr/bin/env python3
"""5. Complex types - list of floats"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """It takes a list of floats as an argument and
    returns the sum as a float.

    Parameters
    ----------
    input_list : List[float]
        floating numbers

    Returns
    -------
    float
        sum of floating numbers
    """
    sum: float = 0

    for i in input_list:
        sum += i

    return sum
