#!/usr/bin/env python3

"""
This module provides a function to create a list of tuples containing strings
and their corresponding lengths.
"""


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Returns a list of tuples where each tuple contains a    string from the
    inputlist and the length of that string.

    Args:
      lst (List[str]): A list of strings.

    Returns:
      List[Tuple[str, int]]: A list of tuples where each    tuple contains a
      stringand its length.
    """
    return [(i, len(i)) for i in lst]
