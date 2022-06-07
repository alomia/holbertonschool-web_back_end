#!/usr/bin/env python3
"""8. Complex types - functions"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Take an argument and return a function that multiplies a float by the argument.

    Parameters
    ----------
    multiplier : float
        number

    Returns
    -------
    float
        returns a function that multiplies a float by the multiplier.
    """

    return lambda x: x * multiplier
