import random


random_engine = random.SystemRandom()


class Item:
    def __init__(self, id: int, name: str, value: float) -> None:
        self.id = id
        self.name = name
        self.value = value


def display_item(item: Item) -> None:
    print(f'Item {item.id}:')
    print(f'  Name: {item.name}')
    print(f'  Value: ${item.value:.2f}')


def random_name() -> str:
    length = random_engine.randint(3, 10)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    name = ''
    for _ in range(length):
        name += alphabet[random_engine.randrange(26)]
    return name


def random_value() -> float:
    return random_engine.random() * 1000


def create_items(count: int) -> list[Item]:
    items: list[Item] = []
    for i in range(count):
        id = i + 1
        name = random_name()
        value = random_value()
        items.append(Item(id, name, value))
    return items


item_count = int(input('How many items? '))
items = create_items(item_count)
for item in items:
    display_item(item)
    print()
