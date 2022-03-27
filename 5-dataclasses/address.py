from dataclasses import dataclass, replace
from datetime import date
from pprint import pprint


@dataclass(frozen=True)
class Address:
    country: str
    state: str
    suburb: str
    street: str
    house_number: int
    unit_number: int | None = None


@dataclass
class Person:
    name: str
    dob: date


addressbook: dict[Address, list[Person]] = {}

address1 = Address('Australia', 'WA', 'Baywater', 'Guildford Rd', 25)
person = Person('Foo Bar', date(2022, 3, 1))
addressbook[address1] = [person]

address2 = replace(address1, house_number=26)
addressbook[address2] = [person]

pprint(addressbook)
