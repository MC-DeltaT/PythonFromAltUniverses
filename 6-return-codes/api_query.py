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
    # return 'ok', 'some data'
    # return 'error', 'timeout'
    # return 'error', HTTPError(404, 'Not found')


match api_query():
    case ('ok', data):
        print(f'Got API data: {data}')
    case ('error', 'timeout'):
        print('Network timeout, retrying...')
        ...
    case ('error', HTTPError(status_code=code)):
        print(f'Got HTTP error code {code}')


match api_query():
    case ('ok', data):
        print(f'Got API data: {data}')
    case ('error', reason):
        print(f'Failed to query API: {reason}')
