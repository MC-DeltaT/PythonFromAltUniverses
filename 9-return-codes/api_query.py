from dataclasses import dataclass
from typing import Literal


Ok = Literal['ok']
Error = Literal['error']

Timeout = Literal['timeout']


@dataclass
class HTTPError:
    status_code: int
    message: str
    
    def __str__(self) -> str:
        return f'HTTP {self.status_code} {self.message}'


APIData = str


def api_query() -> tuple[Ok, APIData] | tuple[Error, Timeout | HTTPError]:
    ...


match api_query():
    case (Ok, data):
        print(f'Got API data: {data}')
    case (Error, Timeout):
        print('Network timeout, retrying...')
        ...
    case (Error, HTTPError(status_code=code)):
        print(f'Got HTTP error code {code}')


match api_query():
    case (Ok, data):
        print(f'Got API data: {data}')
    case (Error, reason):
        print(f'Failed to query API: {reason}')
