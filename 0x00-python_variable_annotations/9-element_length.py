#!/usr/bin/env python3

"""
This module provides a function to create a list of tuples containing strings
and their corresponding lengths.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:

    """
    Returns a list of tuples where each tuple contains
    sequence from the
    input list and the length of that sequence.

    Args:
    lst (Iterable[Sequence]): An iterable of sequences (e.g., strings, lists)

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple contains a
    sequence and its length.
    """

    return [(i, len(i)) for i in lst]
