# polymorphism_demo.py

import math

class Shape:
    """Base class for shapes."""
    def area(self):
        """Method to calculate area, to be overridden by derived classes."""
        raise NotImplementedError("Subclasses must override this method.")


class Rectangle(Shape):
    """A class representing a rectangle."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle (length × width)."""
        return self.length * self.width


class Circle(Shape):
    """A class representing a circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle (π × radius²)."""
        return math.pi * (self.radius ** 2)
