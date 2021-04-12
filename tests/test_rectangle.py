from src.figures import Rectangle
import pytest


def test_rectangle_create(simple_rectangle):
    assert isinstance(simple_rectangle, Rectangle)


def test_rectangle_name(simple_rectangle):
    assert simple_rectangle.name == "Rectangle"


def test_rectangle_angles(simple_rectangle):
    assert simple_rectangle.angles == 4


@pytest.mark.parametrize("a, b", [(12, 1), (3.9, 4.0), (90.1, 34)])
def test_rectangle_perimeter(a, b):
    rectangle = Rectangle(a, b)
    assert rectangle.perimeter == (a + b) * 2


@pytest.mark.parametrize("a, b", [(128, 256.001), (32, 4.0), (4.6, 2.2)])
def test_rectangle_area(a, b):
    rectangle = Rectangle(a, b)
    assert rectangle.area == a * b
