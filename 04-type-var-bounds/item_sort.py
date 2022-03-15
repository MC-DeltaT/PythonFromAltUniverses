from dataclasses import dataclass
from typing import TypeVar


@dataclass
class Item:
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
    Potion(1, 'Healing potion A', 10.0, 50.0),
    Potion(2, 'Healing potion B', 1000.0, 9999.9),
    Potion(3, 'Healing potion C', 30.0, 120.0)
]
potions_sorted = sort_items(potions)
print(potions_sorted)
