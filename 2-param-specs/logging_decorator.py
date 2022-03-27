from datetime import datetime
from functools import wraps
from typing import Callable, ParamSpec, TypeVar


T = TypeVar('T')
P = ParamSpec('P')


def logged(func: Callable[P, T]) -> Callable[P, T]:
    @wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        arg_strings = [str(a) for a in args] + [f'{k}={v}' for k, v in kwargs.items()]
        arg_string = ', '.join(arg_strings)
        print(f'{datetime.now()} | {func.__name__}({arg_string})')
        return func(*args, **kwargs)
    
    return inner


@logged
def insert_order(instrument_id: int, side: str, price: float, volume: int, lifespan: str, auto_hedge: bool) -> None:
    # Send order to exchange, update internal order book, etc
    ...


insert_order(1234, 'BUY', 26673.5, 20, 'GFD', auto_hedge=True)
