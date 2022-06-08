#!/usr/bin/env python3
"""1. Let's execute multiple coroutines
at the same time with async"""


import asyncio

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """Takes two arguments and will generate
    wait_random n times with max_delay argument
    and returns a list in ascending order.

    Parameters
    ----------
    n : int
        integer number
    max_delay : int
        integer number

    Returns
    -------
    random_delay : List
        list of float numbers
    """
    list_delay: List[float] = []
    for count in range(n):
        list_delay.append(await wait_random(max_delay))
    return sorted(list_delay)
