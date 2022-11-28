from calculator.main import main
import pytest


def test_too_many_arguments_exception():
    """
    Test that an Exception is raised when the input string conists of more
    than two comma-separated integers.
    """
    with pytest.raises(ValueError):
        main("1, 2, 3")


def test_two_arguments_no_exception():
    """Test that no Exception is thrown if the number of arguments <= 2."""
    try:
        main("1, 2")
    except ValueError as exc:
        assert False, f"'1, 2' raised an exception {exc}"


def test_non_integer_argument_exception():
    """Test that an Exception is thrown passing a non-integer argument."""
    main("1, X")
