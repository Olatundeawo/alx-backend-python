#!/usr/bin/env python3
"""
    A type annotated  function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    v *= v
    return (k, v)
