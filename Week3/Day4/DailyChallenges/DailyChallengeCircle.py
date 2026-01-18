# Instructions
# The goal is to create a class that represents a simple circle.

# A Circle can be defined by either specifying the radius or the diameter - use a decorator for it.
# The user can query the circle for either its radius or diameter.



# Abilities of a Circle Instance
# Your Circle class should be able to:

# ✅ Compute the circle’s area.
# ✅ Print the attributes of the circle — use a dunder method (__str__ or __repr__).
# ✅ Add two circles together and return a new circle with the new radius — use a dunder method (__add__).
# ✅ Compare two circles to see which is bigger — use a dunder method (__gt__).
# ✅ Compare two circles to check if they are equal — use a dunder method (__eq__).
# ✅ Store multiple circles in a list and sort them — implement __lt__ or other comparison methods.



import math


class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is None and diameter is None:
            raise ValueError("You must provide radius or diameter.")

        if radius is not None and diameter is not None:
            raise ValueError("Provide only one: radius OR diameter (not both).")

        if radius is not None:
            if radius <= 0:
                raise ValueError("Radius must be positive.")
            self._radius = float(radius)

        if diameter is not None:
            if diameter <= 0:
                raise ValueError("Diameter must be positive.")
            self._radius = float(diameter) / 2

    # decorator for radius
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = float(value)

    # decorator for diameter
    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        if value <= 0:
            raise ValueError("Diameter must be positive.")
        self._radius = float(value) / 2

    def area(self):
        return math.pi * (self._radius ** 2)

    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter})"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("Can only add Circle to Circle.")
        return Circle(radius=self.radius + other.radius)

    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius


# -------------------- Tests --------------------
if __name__ == "__main__":
    c1 = Circle(radius=3)
    c2 = Circle(diameter=10)

    print(c1)
    print(c2)

    print("c1 area:", c1.area())
    print("c2 area:", c2.area())

    c3 = c1 + c2
    print("c3 (c1 + c2):", c3)

    print("c1 > c2:", c1 > c2)
    print("c1 == c2:", c1 == c2)

    circles = [c2, c1, c3]
    circles.sort()
    print("Sorted circles:", circles)
