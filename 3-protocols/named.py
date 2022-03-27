from datetime import date
from typing import Protocol


class Named(Protocol):
    @property
    def name(self) -> str:
        raise NotImplementedError()


class Person:
    def __init__(self, name: str, dob: date) -> None:
        self.name = name
        self.dob = dob


def print_name(named: Named) -> None:
    print(named.name)


person = Person('Foo Bar', date(2022, 3, 16))
print_name(person)
