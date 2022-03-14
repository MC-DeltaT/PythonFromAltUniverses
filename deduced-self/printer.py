from abc import ABC, abstractmethod
from typing import TypeVar


TDerived = TypeVar('TDerived', bound='Printer')


class Printer(ABC):
    def print_line(self: TDerived, message: str) -> TDerived:
        self._write(message + '\n')
        return self

    @abstractmethod
    def _write(self, message: str) -> None:
        raise NotImplementedError()


class StdoutPrinter(Printer):
    def print_fancy(self, message: str) -> 'StdoutPrinter':
        return self.print_line(f'~~~ {message} ~~~')

    def _write(self, message: str) -> None:
        print(message, end='')


printer = StdoutPrinter()
printer.print_line('hello world').print_fancy('Deduced self works!')