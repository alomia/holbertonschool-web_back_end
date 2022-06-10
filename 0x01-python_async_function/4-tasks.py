#!/usr/bin/env python3
"""4. Tasks"""


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
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
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
