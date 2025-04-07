"""
Design a Shape Class:

- Create an abstract class called Shape with an abstract method called area().
- Create subclasses for different shapes (e.g., Circle, Rectangle, Triangle) that implement the area() method.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        self.__name = name

    @abstractmethod
    def area(self) -> float: pass


class Circle(Shape):
    def __init__(self, name: str, radius: float) -> None:
        super().__init__(name)
        if not isinstance(radius, (int, float)):
            raise TypeError('Radius must be a number')
        if radius <= 0:
            raise ValueError('Radius must be a positive number')

        self.__radius = radius

    def area(self) -> float:
        return pi * self.__radius ** 2


class Rectangle(Shape):
    def __init__(self, name: str, base: float, height: float) -> None:
        super().__init__(name)

        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError('Measures must be numbers')
        if base <= 0 or height <= 0:
            raise ValueError('Measures must be positive numbers')

        self.__base = base
        self.__height = height

    def area(self) -> float:
        return self.__base * self.__height


class Triangle(Shape):
    def __init__(self, name: str, base: float, height: float) -> None:
        super().__init__(name)

        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError('Measures must be numbers')
        if base <= 0 or height <= 0:
            raise ValueError('Measures must be positive numbers')

        self.__base = base
        self.__height = height

    def area(self) -> float:
        return self.__base * self.__height / 2


if __name__ == '__main__':
    try:
        figures = [
            Circle("Circle", 5),
            Rectangle("Rectangle", 4, 6),
            Triangle("Triangle", 3, 7),
        ]
    except Exception as e:
        print(f'Error: {e}')
    else:
        for figure in figures:
            print(f"{figure.name}\n\t Area: {figure.area():.2f}")
