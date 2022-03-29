
"""
    Bridge é um padrão de projeto estrutural que tem a intenção de desacoplar uma abstração
        de sua implementação, de modo que as duas possam variar e evoluir independentemente.
    O exemplo abaixo é uma implementação de um dispositivo recebendo comandos de um controle remoto,
        onde este dispositivo pode ter N controles e este controle pode ter N dispositivos.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class IRemotoControl(ABC):
    @abstractmethod
    def power(self) -> None:
        pass

    @abstractmethod
    def volume_up(self) -> None:
        pass

    @abstractmethod
    def volume_down(self) -> None:
        pass


class RemoteControl(IRemotoControl):
    def __init__(self, device: IDevice) -> None:
        self._device = device

    def power(self) -> None:
        self._device.power = not self._device.power

    def volume_up(self) -> None:
        self._device.volume += 10

    def volume_down(self) -> None:
        self._device.volume -= 10


class RemoteControlMute(RemoteControl):
    def mute(self) -> None:
        self._device.volume = 0


class IDevice(ABC):
    @property
    @abstractmethod
    def power(self) -> bool:
        pass

    @power.setter
    def power(self, power: bool) -> None:
        pass

    @property
    @abstractmethod
    def volume(self) -> int:
        pass

    @volume.setter
    def volume(self, volume: int) -> None:
        pass


class TV(IDevice):
    def __init__(self) -> None:
        self._power = False
        self._volume = 10
        self.name = self.__class__.__name__

    @property
    def power(self) -> bool:
        return self._power

    @power.setter
    def power(self, power: bool) -> None:
        self._power = power
        power_status = 'ON' if self._power else 'OFF'
        print(f'{self.name} is {power_status}')

    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, volume: int) -> None:
        if not self._power:
            print(f'Please turn on the {self.name} first')
            return
        elif volume > 100 or volume < 0:
            return

        self._volume = volume
        print(f'{self.name} volume: {self._volume}')

    def __str__(self) -> str:
        return f'{self.name}: {self._power}, {self._volume}'


if __name__ == "__main__":
    tv = TV()
    remote = RemoteControl(tv)
    remote.power()
    remote.volume_up()
    remote.volume_up()
    remote.volume_up()
    remote.volume_down()
    remote.volume_down()
    remote.power()
    remote.volume_up()
    print('mute')
    remote = RemoteControlMute(tv)
    remote.power()
    remote.volume_up()
    remote.mute()
