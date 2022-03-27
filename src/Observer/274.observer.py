"""
    Notificação entre objetos,onde uma alteração notifica outros objetos.
    No caso do exemplo abaixo, quando altera uma informação ele envia notificação para os dispositivos
        que estão adicionados
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List


class IObservable(ABC):
    @property
    @abstractmethod
    def state(self) -> Dict:
        pass

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def notify_observer(self) -> None:
        pass


class WeatherStation(IObservable):
    def __init__(self) -> None:
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self) -> Dict:
        return self._state

    @state.setter
    def state(self, state_update: Dict) -> None:
        # Desempaca e adiciona no dict o novo state.
        new_state: Dict = {**self._state, **state_update}
        # Se caso mudou algo no state, atualiza o state e notifica os observers.
        if new_state != self._state:
            self._state = new_state
            print('')
            self.notify_observer()

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def reset_state(self) -> None:
        self._state = {}
        print('')
        self.notify_observer()

    def notify_observer(self) -> None:
        for observer in self._observers:
            observer.update()


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None:
        pass


class Smatphone(IObserver):
    def __init__(self, name, observable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} o objeto {observable_name} acabou de ser atualizado => {self.observable.state}')


class Notebook(IObserver):
    def __init__(self, observable) -> None:
        self.observable = observable

    def update(self) -> None:
        state = self.observable.state
        print(f'sou o note e vou fazer outra coisa', state)


if __name__ == "__main__":
    weather_station = WeatherStation()
    smatphone = Smatphone('IPhone', weather_station)
    smatphone2 = Smatphone('Samsung', weather_station)
    notebook = Notebook(weather_station)

    weather_station.add_observer(smatphone)
    weather_station.add_observer(smatphone2)
    weather_station.add_observer(notebook)

    weather_station.state = {'temperature': 10}
    weather_station.state = {'temperature': 12, 'humidity': 20}
    weather_station.state = {'temperature': 12, 'humidity': 20}
    weather_station.state = {'temperature': 12, 'humidity': 20}
    weather_station.state = {'temperature': 12, 'humidity': 20}
    weather_station.state = {}

    weather_station.remove_observer(smatphone)
    weather_station.reset_state()
