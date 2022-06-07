#!/usr/bin/env python3
"""9. Let's duck type an iterable object"""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns elements of the list with its length

    Parameters
    ----------
    lst : Iterable[Sequence]
        List

    Returns
    -------
    List
        List[Tuple[Sequence]]
    """
    return [(i, len(i)) for i in lst]
