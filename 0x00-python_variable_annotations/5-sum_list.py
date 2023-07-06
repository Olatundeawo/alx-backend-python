#!/usr/bin/env python3
from typing import List
"""
    A type annotated function
"""


def sum_list(input_list: List[float]) -> float:
    """
        function that takes a list of input in float
        and return the sum of the list input
    """
    total = 0
    for x in input_list:
        total += x
    return (total)
