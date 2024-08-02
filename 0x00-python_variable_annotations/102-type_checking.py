#!/usr/bin/env python3

"""
This module provides a function to zoom in on elements of a tuple by repeating
each element a specified number of times.
"""


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:

    """
    Returns a tuple where each element in the input tuple is repeated
    'factor' times.

    Args:
        lst (Tuple[int, ...]): The input tuple.
        factor (int): The factor by which to repeat each element.

    Returns:
        Tuple[int, ...]: A tuple with repeated elements.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
