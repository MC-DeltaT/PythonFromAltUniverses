from dataclasses import dataclass
from typing import Generic, Optional, TypeVar


T = TypeVar('T')


@dataclass
class StackNode(Generic[T]):
    value: T
    next_node: Optional['StackNode[T]']


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[StackNode[T]] = None

    def push(self, value: T) -> None:
        self.head = StackNode(value, self.head)

    def pop(self) -> T:
        if self.head is None:
            raise ValueError('Stack is empty')
        else:
            value = self.head.value
            self.head = self.head.next_node
            return value


stack: Stack[str] = Stack()
stack.push('world!')
stack.push('hello')
item1 = stack.pop()
print(item1)
item2 = stack.pop()
print(item2)
