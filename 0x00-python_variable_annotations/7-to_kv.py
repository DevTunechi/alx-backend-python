#!/usr/bin/env python3

"""
Module provides functn to create a tuple where the first element
is a string key and second element is the square of an integer or float value
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the string k, and the second
    elementis the square of the int or float v.

    Args:
      k (str): The string key.
      v (Union[int, float]): The integer or float value to be squared

    Returns:
      Tuple[str, float]: A tuple with the string k and the square of v
    """

    return (k, float(v ** 2))
