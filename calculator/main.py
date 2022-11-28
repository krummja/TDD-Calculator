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
            pass
        return 0


def main(input: str = "") -> None:
    """Application entrypoint."""
    result = Calculator.add(input)
    print(result)


if __name__ == '__main__':
    main()
