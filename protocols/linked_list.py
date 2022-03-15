from dataclasses import dataclass
from typing import Callable, Generic, Iterable, Iterator, Optional, TypeVar


T = TypeVar('T')


@dataclass
class LinkedListNode(Generic[T]):
    value: T
    next_node: Optional['LinkedListNode[T]']


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[LinkedListNode[T]] = None

    def prepend(self, value: T) -> None:
        self.head = LinkedListNode(value, self.head)
    
    def __iter__(self) -> Iterator[T]:
        node = self.head
        while node:
            yield node.value
            node = node.next_node


def enumerate_iterable(it: Iterable[T], func: Callable[[int, T], None]) -> None:
    for i, item in enumerate(it):
        func(i, item)


linked_list: LinkedList[str] = LinkedList()
linked_list.prepend('world')
linked_list.prepend('hello')
enumerate_iterable(linked_list, lambda i, v: print(f'{i}: {v}'))

assert isinstance(linked_list, Iterable)
