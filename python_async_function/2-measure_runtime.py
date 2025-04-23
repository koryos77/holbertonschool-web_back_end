#!/usr/bin/env python3
"""Create a measure_time function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay),
and returns total_time / n."""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines')


def measure_time(n: int, max_delay: int) -> float:
    """Create a measure_time function with integers n, max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay).

    Args:
        n (int): number of times to spawn wait_random in wait_n
        max_delay (int): Max delay for wait_n
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time

    return total_time
