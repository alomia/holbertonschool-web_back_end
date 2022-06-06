#!/usr/bin/env python3
"""6. Complex types - mixed list"""


from typing import List
import typing


def sum_mixed_list(mxd_lst: List[typing.Union[int, float]]) -> float:
    """It takes a list of floats and integers as an argument
    and returns their sum as a float.

    Parameters
    ----------
    input_list : List
        list of floats and integers

    Returns
    -------
    float
        sum of floating numbers and integers
    """
    sum: float = 0

    for num in mxd_lst:
        sum += num

    return sum
