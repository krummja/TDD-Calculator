from calculator.main import main
import pytest


def test_too_many_arguments_exception():
    main("1, 2, 3")


def test_two_arguments_no_exception():
    main("1, 2")


def test_non_integer_argument_exception():
    main("1, X")
