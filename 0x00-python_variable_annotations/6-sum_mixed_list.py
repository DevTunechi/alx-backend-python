#!/usr/bin/env python3

"""
Module provides a function to sum a list of integers and floats
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and floats and returns the result.

    Args:
      mxd_lst (List[Union[int, float]]): A list of integers and floats to sum

    Returns:
      float: The sum of the integers and floats in the list.
    """
    return float(sum(mxd_lst))
