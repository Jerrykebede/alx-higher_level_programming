#!/usr/bin/python3
''' models/rectangle.py'''

from models.base import Base


class Rectangle(Base):
    """Class representing a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        self.validate_dimension(value, "width")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        self.validate_dimension(value, "height")
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        self.validate_coordinate(value, "x")
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        self.validate_coordinate(value, "y")
        self.__y = value

    def validate_dimension(self, value, attribute_name):
        """Validate if the dimension value is valid."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")

    def validate_coordinate(self, value, attribute_name):
        """Validate if the coordinate value is valid."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        elif value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")

    def update(self, *args, **kwargs):
        """Update the attributes of the Rectangle."""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Return the string representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Display the rectangle with '#' characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
