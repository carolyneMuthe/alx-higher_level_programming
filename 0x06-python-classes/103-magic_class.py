#!/usr/bin/python3
import math


class MagicClass:
    """A class that represents a circle with radius, area,
          and circumference."""

    def __init__(self, radius=0):
        """
        Initialize the MagicClass with a radius.

        Args:
            radius (int, float): The radius of the circle.

        Raises:
            TypeError: If radius is not a number.
            ValueError: If radius is less than 0.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        if radius < 0:
            raise ValueError("radius must be >= 0")

        self.__radius = radius  # Set the radius

    def area(self):
        """Calculate and return the area of the circle."""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.__radius
