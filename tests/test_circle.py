from src.figures import Circle
from math import pi
import pytest


def test_circle_create(simple_circle):
    assert isinstance(simple_circle, Circle)


def test_circle_name(simple_circle):
    assert simple_circle.name == "Circle"


def test_circle_angles(simple_circle):
    assert simple_circle.angles == 0


@pytest.mark.parametrize("r", [1, 3, 34.33])
def test_circle_perimeter(r):
    circle = Circle(r)
    assert circle.perimeter == 2 * pi * r


@pytest.mark.parametrize("r", [128, 32, 11.99])
def test_circle_area(r):
    circle = Circle(r)
    assert circle.area == pi * r * r
