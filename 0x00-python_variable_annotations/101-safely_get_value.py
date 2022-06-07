#!/usr/bin/env python3
"""10. Duck typing - first element of a sequence"""


from typing import Any, Mapping, TypeVar, Union


def safely_get_value(dct: Mapping, key: Any, default: Union[TypeVar('T'), None] = None) -> Union[Any, TypeVar('T')]:
    """Given the parameters and the return values

    Parameters
    ----------
    dct : Mapping
    key : Any
    default: Union[TypeVar('T'), None] = None

    Returns
    -------
    Mapping
        Union[Any, TypeVar('T')]
    """
    if key in dct:
        return dct[key]
    else:
        return default
