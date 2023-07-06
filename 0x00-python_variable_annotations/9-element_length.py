#!/usr/bin/env python3
"""
    type annotation function
"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """A function """
    return [(i, len(i)) for i in lst]
