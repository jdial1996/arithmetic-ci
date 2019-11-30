import pytest
from arithmetic import Arithmetic

test_object = Arithmetic(4, 3)


def test_initial_values():
    assert test_object.num1 == 4
    assert test_object.num2 == 3


def test_addition():
    assert test_object.addition() == 7


def test_subtraction():
    assert test_object.subtraction() == 1


def test_multiplication():
    assert test_object.multiplication() == 12


def test_division():
    assert test_object.division() == 4 / 3
