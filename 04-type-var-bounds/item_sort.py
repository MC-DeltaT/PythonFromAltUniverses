from abc import ABC
from dataclasses import dataclass
from typing import TypeVar


@dataclass
class Item(ABC):
    id: int
    name: str
    value: float


@dataclass
class Potion(Item):
    heal_amount: float


TItem = TypeVar('TItem', bound=Item)


def sort_items(items: list[TItem]) -> list[TItem]:
    return sorted(items, key=lambda i: (i.name, -i.value))


potions = [
    Potion(1, 'Healing potion', 10.0, 50.0),
    Potion(2, 'Max heal', 1000.0, 9999.9),
    Potion(3, 'Decent potion', 30.0, 120.0)
]
potions_sorted = sort_items(potions)
print(potions_sorted[1].heal_amount)
