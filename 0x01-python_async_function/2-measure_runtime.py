#!/usr/bin/env python3
""" Measures the runtime """
import asyncio
import time
from typing import Union


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        Measures the average runtime of wait_n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()

    return (end - start) / n
