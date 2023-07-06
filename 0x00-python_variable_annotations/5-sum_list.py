#!/usr/bin/env python3
"""
    A type annotated function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Function that takes a list of input in float
        and return the sum of the list input
    """
    total = 0
    for x in input_list:
        total += x
    return (total)
