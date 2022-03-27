from typing import Callable, Generic, Iterable, Iterator, Protocol, runtime_checkable, TypeVar


TCo = TypeVar('TCo', covariant=True)
T = TypeVar('T')


@runtime_checkable
class SizedIterable(Protocol, Generic[TCo]):
    def __iter__(self) -> Iterator[TCo]:
        raise NotImplementedError()

    def __len__(self) -> int:
        raise NotImplementedError()


class SizedMap(Generic[T]):
    def __init__(self, func: Callable[[TCo], T], iterable: SizedIterable[TCo]) -> None:
        self._func = func
        self._iterable = iterable

    def __iter__(self) -> Iterator[T]:
        return map(self._func, self._iterable)

    def __len__(self) -> int:
        return len(self._iterable)


def use_size(iterable: Iterable[int]) -> None:
    if not isinstance(iterable, SizedIterable):
        # Don't enumerate all elements if we don't need to
        iterable = list(iterable)
    size = len(iterable)
    print(size)
    ...


m1 = SizedMap(lambda x: x + 1, range(1_000_000_000))
m2 = SizedMap(lambda x: x * 2, m1)
use_size(m2)
