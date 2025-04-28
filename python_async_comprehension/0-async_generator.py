#!/usr/bin/env python3
"""
Coroutine called async_generator that takes no arguments.
"""


import random
import asyncio


async def async_generator():
    """The coroutine will loop 10 times, each time asynchronously
    wait 1 second, then yield a random number between 0 and 10. 

    Yields:
        Float: Random number between 0 and 10
    """
    for i in range(10):
        i = random.uniform(0, 11)
        yield i
        await asyncio.sleep(1)
