#!/usr/bin/env python3

"""
This module provides a function to safely return the first element of a
sequence or None if the sequence is empty.
"""


from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of the sequence if it exists, otherwise None.

    Args:
    lst (Sequence[Any]): A sequence of elements of any type.

    Returns:
    Optional[Any]: The first element of the sequence, or    None if the
    sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
