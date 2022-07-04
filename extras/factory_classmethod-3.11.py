from typing import Iterable, Self


class Array:
    def __init__(self, size: int) -> None:
        ...

    def __getitem__(self, index: int) -> int:
        ...

    def __setitem__(self, index: int, value: int) -> None:
        ...

    @classmethod
    def from_iterable(cls, iterable: Iterable[int]) -> Self:
        elements = list(iterable)
        array = cls(len(elements))
        for i, elem in enumerate(elements):
            array[i] = elem
        return array


class FlexibleArray(Array):
    def resize(self, new_size: int) -> None:
        ...


array = FlexibleArray.from_iterable([1, 2, 3])
array.resize(10)
