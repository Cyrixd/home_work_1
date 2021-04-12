from tests.conftest import *
from itertools import *


def test_unable_to_create_an_instance_of_figure():
    with pytest.raises(TypeError):
        fig = Figure()


def test_add_area_method_positive(simple_triangle, simple_rectangle, simple_square, simple_circle):
    for fig_a, fig_b in combinations_with_replacement(
            (simple_triangle, simple_rectangle, simple_square, simple_circle), 2):
        assert fig_a.add_area(fig_b) == fig_a.area + fig_b.area


def test_add_area_method_negative(simple_triangle, simple_rectangle, simple_square, simple_circle):
    for figure in (simple_triangle, simple_rectangle, simple_square, simple_circle):
        with pytest.raises(Exception):
            figure.add_area(int)
