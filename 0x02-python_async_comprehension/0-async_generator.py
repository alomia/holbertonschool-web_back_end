#!/usr/bin/env python3
"""0x02. Python - Async Comprehension"""


import asyncio
import random


async def async_generator() -> float:
    """The coroutine will loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.

    Parameters
    ----------

    Returns
    -------
    random.uniform(0, 10)
        random floating number
    """
    for count in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
