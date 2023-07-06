#!/usr/bin/env python3
"""
    A type annonated function
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ A function that takes an argument in two different
        type(int, float) and return the arugment in a single type(float)
    """
    total = 0
    for x in mxd_lst:
        total += x
    return float(total)
