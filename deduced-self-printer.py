from typing import TypeVar
from abc import ABC, abstractmethod


TDerived = TypeVar('TDerived', bound='BasePrinter')


class BasePrinter(ABC):
    def print(self: TDerived, message: str) -> TDerived:
        self._write(message)
        return self

    def print_line(self: TDerived, message: str) -> TDerived:
        return self.print(message + '\n')

    @abstractmethod
    def _write(self, message: str) -> None:
        raise NotImplementedError()


class StdoutPrinter(BasePrinter):
    def print_fancy(self, message: str) -> 'StdoutPrinter':
        return self.print_line(f'~~~ {message} ~~~')

    def _write(self, message: str) -> None:
        print(message, end='')


printer = StdoutPrinter()
printer.print('hello').print_line(' world').print_fancy('CRTP works!')
