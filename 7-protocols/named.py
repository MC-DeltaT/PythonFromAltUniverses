from dataclasses import dataclass
from datetime import date
from typing import Protocol


class Named(Protocol):
    @property
    def name(self) -> str:
        raise NotImplementedError()


@dataclass
class Person:
    name: str
    dob: date


def print_name(named: Named) -> None:
    print(named.name)


person = Person('Foo Bar', date(2022, 3, 16))
print_name(person)
