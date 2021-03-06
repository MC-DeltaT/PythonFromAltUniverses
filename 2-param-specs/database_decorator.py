from functools import wraps
from typing import Callable, Concatenate, ParamSpec, TypeVar


T = TypeVar('T')
P = ParamSpec('P')


class DatabaseConnection:
    ...


def with_database(func: Callable[Concatenate[DatabaseConnection, P], T]) -> Callable[P, T]:
    # Note P does not include DatabaseConnection
    @wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        database_connection = DatabaseConnection()
        return func(database_connection, *args, **kwargs)
    
    return inner


@with_database
def get_users(database_connection: DatabaseConnection, country: str) -> ...:
    print(f'db={database_connection}, {country=}')
    ...


get_users('Australia')
