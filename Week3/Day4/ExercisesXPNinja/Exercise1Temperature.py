# Instructions
# Write a base class called Temperature.
# Implement the following subclasses: Celsius, Kelvin, Fahrenheit.
# Each of the subclasses should have a method which can convert the temperture to another type.
# You must consider different designs and pick the best one according to the SOLID Principle.



from __future__ import annotations
from abc import ABC, abstractmethod


class Temperature(ABC):
    def __init__(self, value: float):
        self.value = float(value)

    @abstractmethod
    def to_celsius(self) -> float:
        pass

    @classmethod
    @abstractmethod
    def from_celsius(cls, c: float) -> "Temperature":
        pass

    def convert_to(self, target_cls: type["Temperature"]) -> "Temperature":
        if not issubclass(target_cls, Temperature):
            raise TypeError("target_cls must be a Temperature subclass.")
        c = self.to_celsius()
        return target_cls.from_celsius(c)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value})"


class Celsius(Temperature):
    def to_celsius(self) -> float:
        return self.value

    @classmethod
    def from_celsius(cls, c: float) -> "Celsius":
        return cls(c)


class Kelvin(Temperature):
    def to_celsius(self) -> float:
        return self.value - 273.15

    @classmethod
    def from_celsius(cls, c: float) -> "Kelvin":
        return cls(c + 273.15)


class Fahrenheit(Temperature):
    def to_celsius(self) -> float:
        return (self.value - 32) * 5 / 9

    @classmethod
    def from_celsius(cls, c: float) -> "Fahrenheit":
        return cls(c * 9 / 5 + 32)


# Demo
if __name__ == "__main__":
    t = Fahrenheit(98.6)
    print(t, "->", t.convert_to(Celsius), "->", t.convert_to(Kelvin))
