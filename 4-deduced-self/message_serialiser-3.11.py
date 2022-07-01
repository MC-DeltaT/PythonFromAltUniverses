from datetime import datetime
from typing import Self


class MessageSerialiser:
    def set_source(self, source: str) -> Self:
        ...
        return self

    def set_timestamp(self, timestamp: datetime) -> Self:
        ...
        return self

    def as_bytes(self) -> bytes:
        ...


class RequestSerialiser(MessageSerialiser):
    def set_request_param(self, param: str) -> Self:
        ...
        return self


message = (
    RequestSerialiser()
    .set_source('My PC')
    .set_timestamp(datetime.now())
    .set_request_param('give me the data!')
    .as_bytes())
