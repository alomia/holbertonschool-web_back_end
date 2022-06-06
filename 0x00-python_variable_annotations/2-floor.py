#!/usr/bin/env python3
"""2. Basic annotations - floor"""


def floor(n: float) -> int:
    """Takes a float n as an argument and
    returns the floor of the float.

    Parameters
    ----------
    n : float
        number

    Returns
    -------
    int
        floor
    """
    nStr = str(n)
    if int(nStr[0]) > 0:
        n = int(nStr[0])
    else:
        n = int(nStr[0] + -1)

    return n
