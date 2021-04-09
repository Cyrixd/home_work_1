from src.figures import Square
import pytest


def test_square_create(simple_square):
    assert isinstance(simple_square, Square)


def test_square_name(simple_square):
    assert simple_square.name == "Square"


def test_square_angles(simple_square):
    assert simple_square.angles == 4


@pytest.mark.parametrize("a", [1, 2, 4.1])
def test_square_perimeter(a):
    square = Square(a)
    assert square.perimeter == a * 4


@pytest.mark.parametrize("a", [1, 2, 9.9])
def test_square_area(a):
    square = Square(a)
    assert square.area == a ** 2
