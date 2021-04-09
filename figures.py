from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):
    @property
    @abstractmethod
    def angles(self):
        return 0

    @property
    @abstractmethod
    def perimeter(self):
        return 0

    @property
    @abstractmethod
    def area(self):
        return 0

    @property
    def name(self):
        return self.__class__.__name__

    def __str__(self):
        return f"Name = {self.name};\
                Angles = {self.angles};\
                Perimeter = {self.perimeter};\
                Area = {self.area}"

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise Exception(f"Object {figure} is not a geometric figure.")
        return self.area + figure.area


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    @property
    def angles(self):
        return 3

    @property
    def perimeter(self):
        return self._side_a + self._side_b + self._side_c

    @property
    def area(self):
        _p = self.perimeter / 2
        return (_p * (_p - self._side_a) * (_p - self._side_b) * (_p - self._side_c)) ** 0.5


class Rectangle(Figure):
    def __init__(self, _side_a, _side_b):
        self._side_a = _side_a
        self._side_b = _side_b

    @property
    def angles(self):
        return 4

    @property
    def perimeter(self):
        return (self._side_a + self._side_b) * 2

    @property
    def area(self):
        return self._side_a * self._side_b


class Square(Rectangle):
    def __init__(self, _side_a):
        super().__init__(_side_a, _side_a)


class Circle(Figure):
    def __init__(self, r):
        self._r = r

    @property
    def angles(self):
        return 0

    @property
    def perimeter(self):
        return 2 * pi * self._r

    @property
    def area(self):
        return pi * self._r * self._r


tri = Triangle(3, 4, 5)
print(tri)

rect = Rectangle(10, 2)
print(rect)

sq = Square(10)
print(sq)

cir = Circle(2)
print(cir)

print(tri.add_area(cir))
