import pytest
from src.figures import *


@pytest.fixture
def simple_triangle():
    return Triangle(3, 4, 5)


@pytest.fixture
def simple_rectangle():
    return Rectangle(2, 1)


@pytest.fixture
def simple_square():
    return Square(1)


@pytest.fixture
def simple_circle():
    return Circle(1)
