#!/usr/bin/env python3
"""
    A type annotated function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ A function that returns a function that
        multiply the argument of the main function
    """
    return lambda x: x * multiplier
