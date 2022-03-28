"""
    É um objeto de fachada é um objeto que contém uma interface para um conjunto de objetos.
    O objetivo dele é retirar a complexidade do código e facilitar a implementação, implementando
        classes mais dirretas e simples para a utilização.
    O exemplo abaixo foi retirado do Observer > 274.observer.py, e só foi implementado a classe: WeatherStationFacade 
    Mas se o cliente quiser implementar o sistema 'complexo' ele pode ainda implementar.
"""

from __future__ import annotations
from typing import Dict, List
from abc import ABC, abstractmethod


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


class WeatherStationFacade:
    # Este é o objeto de fachada, que contém uma interface para um conjunto de objetos.
    def __init__(self) -> None:
        self.weather_station = WeatherStation()
        self.smatphone = Smatphone('IPhone', self.weather_station)
        self.smatphone2 = Smatphone('Samsung', self.weather_station)
        self.notebook = Notebook(self.weather_station)

        self.weather_station.add_observer(self.smatphone)
        self.weather_station.add_observer(self.smatphone2)
        self.weather_station.add_observer(self.notebook)

    def add_observer(self, observer: IObserver) -> None:
        self.weather_station.add_observer(observer)

    def remove_observer(self, observer: IObserver) -> None:
        self.weather_station.remove_observer(observer)

    def change_state(self, state: Dict) -> None:
        self.weather_station.state = state

    def reset_state(self) -> None:
        self.weather_station.reset_state()


if __name__ == "__main__":
    weather_station = WeatherStationFacade()

    weather_station.change_state({'temperature': 10})
    weather_station.change_state({'temperature': 20})
    weather_station.change_state({'himidity': 90})

    weather_station.remove_observer(weather_station.smatphone)
    weather_station.change_state({'himidity': 50})
