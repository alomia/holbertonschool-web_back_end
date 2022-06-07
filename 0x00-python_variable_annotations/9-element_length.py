#!/usr/bin/env python3
"""9. Let's duck type an iterable object"""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence]]:
    """Take an argument and return a function that multiplies
    a float by the argument.

    Parameters
    ----------
    lst : Iterable[Sequence]

    Returns
    -------
    List
        List[Tuple[Sequence]]
    """
    return [(i, len(i)) for i in lst]
