#!/usr/bin/env python3

"""
This module provides a function to safely get a value from a dictionary
with a specified key or return a default value if the key is not found.
"""


from typing import TypeVar, Mapping, Any, Optional


T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default: Optional[T] =
                     None) -> Optional[T]:
    """
    Safely retrieves a value from a dictionary.

    Args:
        dct (Mapping[Any, T]): The dictionary to retrieve the value from.
        key (Any): The key to look for in the dictionary.
        default (Optional[T]): The default value to
        return if the key is not found.

    Returns:
        Optional[T]: The value associated with the key if found, otherwise the
        default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
