from typing import TypeVar, Generic
from abc import ABC, abstractmethod


TDerived = TypeVar('TDerived', bound='BasePrinter')


class BasePrinter(Generic[TDerived], ABC):
    def print(self, message: str) -> TDerived:
        self._print(message)
        return self

    def print_line(self, message: str) -> TDerived:
        self._print(message + '\n')
        return self

    @abstractmethod
    def _print(self, message: str) -> None:
        raise NotImplementedError()


class StdoutPrinter(BasePrinter['StdoutPrinter']):
    def print_fancy(self, message: str) -> 'StdoutPrinter':
        print(f'~~~ {message} ~~~')
        return self

    def _print(self, message: str) -> None:
        print(message, end='')


printer = StdoutPrinter()
printer.print('hello').print_line(' world').print_fancy('CRTP works!')
