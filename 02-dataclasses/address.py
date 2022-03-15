from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class Address:
    country: str
    state: str
    suburb: str
    street: str
    house_number: int
    unit_number: Optional[int] = None


@dataclass
class Person:
    name: str
    dob: date


addressbook: dict[Address, list[Person]] = {}

address = Address('Australia', 'WA', 'Perth', 'Francis St', 25)
person = Person('Foo Bar', date(2022, 3, 1))
addressbook[address] = [person]
print(addressbook)
