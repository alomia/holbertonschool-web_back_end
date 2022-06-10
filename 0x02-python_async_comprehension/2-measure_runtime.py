#!/usr/bin/env python3
"""1. Async Comprehensions"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run time for four parallel comprehensions

    Parameters
    ----------

    Returns
    -------
    total_time : float
        float number
    """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time
