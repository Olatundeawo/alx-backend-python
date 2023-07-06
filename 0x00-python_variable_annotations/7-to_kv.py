#!/usr/bin/env python3
"""
    A type annotated  function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ a function that takes two argument in
        the second argument is either float or int
        and return a tuple of str or float
    """
    v *= v
    return (k, v)
