#!/usr/bin/env python3
"""3. Tasks"""


import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int):
    """It takes an integer and returns an asyncio.Task.

    Parameters
    ----------
    max_delay : int
        integer number

    Returns
    -------
    asyncio.Task
        <class '_asyncio.Task'>
    """
    return asyncio.Task(wait_random(max_delay))
