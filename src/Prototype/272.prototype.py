
"""
    Clonar classes
"""

from ast import Str
from typing import List
from copy import deepcopy


class StringReprMixing:
    def __str__(self):
        parms = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])

        return f'{self.__class__.__name__}({parms})'

    def __repr__(self) -> str:
        return self.__str__()


class Person(StringReprMixing):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.addresses: List = []

    def add_address(self, address):
        self.addresses.append(address)


class Address(StringReprMixing):
    def __init__(self, street: str, number: int) -> None:
        self.street: str = street
        self.number: int = number


if __name__ == '__main__':

    p1 = Person('Eliézer', 30)
    p1.add_address(Address('Rua 1', 1))
    # Realizando a cópia profunda de um objeto para o outro ou seja clonar
    esposa_p1 = deepcopy(p1)
    esposa_p1.name = 'Maria'

    print(p1)
    print(esposa_p1)
