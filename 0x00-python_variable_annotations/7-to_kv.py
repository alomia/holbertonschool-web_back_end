#!/usr/bin/env python3
"""7. Complex types - string and int/float to tuple"""


from typing import Union
from typing import Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """It takes two arguments, a string and a number, integer or float,
    and returns a tuple.

    Parameters
    ----------
    k : str
        string
    V : int or float
        integer or floating number

    Returns
    -------
    Tuple
        the first element of the tuple is the string k,
        the second is the square of the int/float v.
    """
    return k, (v * v)
