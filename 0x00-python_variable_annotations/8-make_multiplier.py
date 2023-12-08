#!/usr/bin/env python3
"""
provides a function for creating a function that
    multiplies a float by a multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function takes a float as an argument and returns a function that
        multiplies a float by the multiplier

    Parameters:
    multiplier (float): The multiplier

    Returns:
    Callable[[float], float]: A function that multiplies a float by the
        multiplier
    """
    def multiply(n: float) -> float:
        """
        function multiplies a float by the multiplier

        Parameters:
        n (float): The float to multiplier

        Returns:
        float: multiplied n 
        """
        return n * multiplier
    return multiply
