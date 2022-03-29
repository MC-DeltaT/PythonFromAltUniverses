from typing import Generic, Iterable, Iterator, Protocol, runtime_checkable, TypeVar


TCo = TypeVar('TCo', covariant=True)


@runtime_checkable
class SizedIterable(Protocol, Generic[TCo]):
    def __iter__(self) -> Iterator[TCo]:
        raise NotImplementedError()

    def __len__(self) -> int:
        raise NotImplementedError()


def use_size(iterable: Iterable[int]) -> None:
    if not isinstance(iterable, SizedIterable):
        # Don't enumerate all elements if we don't need to
        iterable = list(iterable)
    size = len(iterable)
    print(size)
    ...


use_size(range(1_000_000_000))
