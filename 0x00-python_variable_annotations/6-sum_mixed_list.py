#!/usr/bin/env python3
from typing import List, Union
"""
    A type annonated function
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    total = 0
    for x in mxd_lst:
        total += x
    return float(total)
