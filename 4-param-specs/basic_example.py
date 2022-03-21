from typing import Callable, ParamSpec, TypeVar


T = TypeVar('T')
P = ParamSpec('P')


def wrapper(func: Callable[P, T]) -> Callable[P, T]:
    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        return func(*args, **kwargs)
    
    return inner


def func(i: int, s: str) -> float:
    print(i)
    print(s)
    return 3.14


wrapped_func = wrapper(func)
ret = wrapped_func(42, 'foo')
