from calculator.main import main
import pytest
import re


def test_too_many_arguments_exception():
    """
    Test that an Exception is raised when the input string conists of more
    than two comma-separated integers.
    """
    message: str = "Input list must consist of 0, 1, or 2 integers."
    
    with pytest.raises(ValueError, match=message):
        main("1, 2, 3")


def test_two_arguments_no_exception():
    """Test that no Exception is thrown if the number of arguments <= 2."""
    try:
        main("1, 2")
    except ValueError as exc:
        assert False, f"'1, 2' raised an exception {exc}"


def test_string_argument_exception():
    """Test that an Exception is thrown passing a non-integer argument."""
    message: str = r"invalid literal for int\(\) with base 10: ' [A-Za-z]*"
    with pytest.raises(ValueError, match=message):
        main("1, X")
