#!/usr/bin/env python3
"""2. Measure the runtime"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the execution time of wait_n and
    return total time.

    Parameters
    ----------
    n : int
        integer number
    max_delay : int
        integer number

    Returns
    -------
    total_time : float
        float number
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time: float = end_time - start_time
    return total_time
