from calculator.main import main
import pytest


it_works = True


def test_basic_testing():
    assert it_works == True
    main("1, 2, 3")
