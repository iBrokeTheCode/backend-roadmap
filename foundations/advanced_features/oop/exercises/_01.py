"""
Create a Class Hierarchy:

- Design a class hierarchy for different types of vehicles (e.g., Car, Truck, Motorcycle).
- Include attributes and methods specific to each vehicle type.
- Include an abstract class called Vehicle, and make the other classes inherit from it.
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Abstract base class for vehicles."""

    def __init__(self, manufacturer: str) -> None:
        self.__manufacturer = manufacturer

    @abstractmethod
    def get_info(self) -> str: pass

    @property
    def manufacturer(self) -> str:
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer: str) -> None:
        self.__manufacturer = manufacturer


class Car(Vehicle):
    def __init__(self, manufacturer: str, doors: int) -> None:
        super().__init__(manufacturer)
        self.__doors = doors

    @property
    def doors(self) -> int:
        return self.__doors

    @doors.setter
    def doors(self, doors: int) -> None:
        if doors < 0:
            raise ValueError('Number of doors cannot be negative')
        self.__doors = doors

    def get_info(self) -> str:
        """Returns information about the vehicle."""

        return f'Car: \n\tManufacturer: {self.manufacturer}, \n\tDoors: {self.doors}'


class Truck(Vehicle):
    def __init__(self, manufacturer: str, size: str) -> None:
        super().__init__(manufacturer)
        self.__size = size

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str) -> None:
        self.__size = size

    def get_info(self) -> str:
        """Returns information about the vehicle."""

        return f'Truck: \n\tManufacturer: {self.manufacturer}, \n\tSize: {self.size}'


class Motorcycle(Vehicle):
    def __init__(self, manufacturer: str,  type: str) -> None:
        super().__init__(manufacturer)
        self.__type = type

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str) -> None:
        self.__type = type

    def get_info(self) -> str:
        """Returns information about the vehicle."""

        return f'Motorcycle: \n\tManufacturer: {self.manufacturer}, \n\tType: {self.type}'


if __name__ == '__main__':
    vehicles = [
        Car('Toyota', 4),
        Truck('Ford', 'Large'),
        Motorcycle('Harley-Davidson', 'Cruiser')
    ]

    for vehicle in vehicles:
        print(vehicle.get_info())
