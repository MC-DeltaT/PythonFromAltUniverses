from datetime import datetime
from typing import TypeVar


T = TypeVar('T', bound='MessageSerialiser')


class MessageSerialiser:
    def set_source(self: T, source: str) -> T:
        ...
        return self

    def set_timestamp(self: T, timestamp: datetime) -> T:
        ...
        return self

    def as_bytes(self) -> bytes:
        ...


class RequestSerialiser(MessageSerialiser):
    def set_request_param(self, param: str) -> 'RequestSerialiser':
        ...
        return self


message = (
    RequestSerialiser()
    .set_source('My PC')
    .set_timestamp(datetime.now())
    .set_request_param('give me the data!')
    .as_bytes())
