#!/usr/bin/env python3
"""3. Tasks"""


import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """It takes an integer and returns an asyncio.Task.

    Parameters
    ----------
    max_delay : int
        integer number

    Returns
    -------
    create_task
        <class '_asyncio.Task'>
    """
    return asyncio.create_task(wait_random(max_delay))
