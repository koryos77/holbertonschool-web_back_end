#!/usr/bin/env python3
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with string k and squared float v"""
    return (k, float(v ** 2))
