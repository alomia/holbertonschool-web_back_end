#!/usr/bin/env python3
"""10. Duck typing - first element of a sequence"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the elements of the list at index 0

    Parameters
    ----------
    lst : Sequence[Any]
        List

    Returns
    -------
    List
        Union[Any, None]
    """
    if lst:
        return lst[0]
    else:
        return None
