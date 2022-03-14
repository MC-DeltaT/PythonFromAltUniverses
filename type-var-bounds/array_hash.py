from typing import Hashable, Iterable, TypeVar


THashable = TypeVar('THashable', bound=Hashable)


def array_hash(array: Iterable[THashable]) -> int:
    # Hash function by Daniel J. Bernstein
    result = 5381
    for element in array:
        result = result * 33 + hash(element)
    return result


array = [1, 4, 67, 5346, 23]
h = array_hash(array)
print(h)
