#!/usr/bin/env python3
"""
provides a function for finding the length of each
    element in a list of strings.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """

    """
    return [(i, len(i)) for i in lst]
