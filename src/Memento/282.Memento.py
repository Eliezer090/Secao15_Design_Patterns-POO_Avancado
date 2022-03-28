
"""
    Realizar backup de estados, este é o objetivo do padrão Memento.
    Abaixo é apresentado uma forma de realizar os backups e restores de estados.
"""

from __future__ import annotations
from copy import deepcopy
from typing import Dict, List


class Memento:
    def __init__(self, state: Dict) -> None:
        self.state: Dict
        super().__setattr__('state', state)

    def getstate(self) -> Dict:
        return self.state

    def __setattr__(self, __name: str, __value) -> None:
        raise AttributeError('Sorry, Memento is immutable')


class ImageEditor:
    def __init__(self, name: str, width: int, height: int) -> None:
        self.name: str = name
        self.width: int = width
        self.height: int = height

    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.getstate()

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.name},{self.width},{self.height})'


class CareTaker:
    def __init__(self, originator: ImageEditor) -> None:
        self._originator: ImageEditor = originator
        self._mementos: List[Memento] = []

    def backup(self) -> None:
        self._mementos.append(self._originator.save_state())

    def restore(self) -> None:
        # print(self._mementos)
        if len(self._mementos) > 0:
            self._originator.restore(self._mementos.pop())


if __name__ == "__main__":
    img = ImageEditor('image', 111, 111)
    caretaker = CareTaker(img)
    caretaker.backup()
    img.name = 'image2'
    img.width = 222
    img.height = 222
    caretaker.backup()

    img.name = 'image5'
    img.width = 555
    img.height = 555
    caretaker.backup()

    caretaker.restore()
    caretaker.restore()
    caretaker.restore()
    caretaker.restore()
    caretaker.restore()
    print(img)
