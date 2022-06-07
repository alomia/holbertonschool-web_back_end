#!/usr/bin/env python3
"""11. More involved type annotations"""


from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Given the parameters and the return values

    Parameters
    ----------
    dct : Mapping
    key : Any
    default : Union[T, None]

    Returns
    -------
    Mapping
        Union[Any, T] value in key position of dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
