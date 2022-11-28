from __future__ import annotations
from beartype.typing import *


class Calculator:

    @staticmethod
    def add(input: str = "") -> int:
        """
        Add together a string representation of comma-separated list of 
        integers.
        """
        if input:
            arguments = Calculator.parse_input(input)
            
            if len(arguments) > 2:
                message: str = "Input list must consist of 0, 1, or 2 integers."
                raise ValueError(message)

            if any([not isinstance(arg, int) for arg in arguments]):
                message: str = "Input list must consist solely of integers."
                raise ValueError(message)
            
            return sum(arguments)
        
        return 0

    @staticmethod
    def parse_input(input: str) -> list[int]:
        """Parse a comma-separated list of strings into a list of integers."""
        return [int(arg) for arg in input.split(",")]


def main(input: str = "") -> None:
    """Application entrypoint."""
    result = Calculator.add(input)
    print(result)
