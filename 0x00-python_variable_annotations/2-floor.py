#!/usr/bin/env python3

"""
This module provides a function to calculate the floor of a float.
"""


import math


def floor(n: float) -> int:
    """
    Returns the floor of a float.

    Args:
      n (float): The float number to floor.

    Returns:
      int: The largest integer less than or equal to n.
    """
    return math.floor(n)
