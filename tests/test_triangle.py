from src.figures import Triangle
import pytest


def test_triangle_create(simple_triangle):
    assert isinstance(simple_triangle, Triangle)


def test_triangle_name(simple_triangle):
    assert simple_triangle.name == "Triangle"


def test_triangle_angles(simple_triangle):
    assert simple_triangle.angles == 3


@pytest.mark.parametrize("a, b, c", [(1, 1, 1), (3, 4.2, 5), (90, 34, 1)])
def test_triangle_perimeter(a, b, c):
    triangle = Triangle(a, b, c)
    assert triangle.perimeter == a + b + c


@pytest.mark.parametrize("a, b, c", [(128, 256, 512.1), (32, 4.2, 2), (46, 22, 1)])
def test_triangle_area(a, b, c):
    triangle = Triangle(a, b, c)
    p = (a + b + c) / 2
    expected_area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    assert triangle.area == expected_area
