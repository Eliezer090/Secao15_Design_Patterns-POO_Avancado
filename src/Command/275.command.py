"""
    Disparar comandos, um exemplo é um controle inteligente onde temos que definir as funções que será feito.
    Cliente -> Invoker -> Reciver -> Command
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from ast import If
from typing import Dict


class Light:
    """Reciver"""

    def __init__(self, name: str, room_name: str) -> None:
        self._name = name
        self._room_name = room_name
        self._state = False
        self.color = 'default color'

    def on(self) -> None:
        self._state = True
        print(f'{self._name} ligado')

    def off(self) -> None:
        self._state = False
        print(f'{self._name} desligado')

    def change_color(self, color: str) -> None:
        self.color = color
        print(f'{self._name} mudou de cor para {self.color}')

    def get_state(self) -> bool:
        return self._state


class ICommand(ABC):
    """Abstract method - Interface the command"""
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class LightOnCommand(ICommand):
    """Concrete method"""

    def __init__(self, light: Light) -> None:
        self._light = light

    def execute(self) -> None:
        self._light.on()

    def undo(self) -> None:
        self._light.off()


class LightChangeColor(ICommand):
    """Concrete method"""

    def __init__(self, light: Light, color: str) -> None:
        self._light = light
        self._color = color
        self._old_collor = self._light.color

    def execute(self) -> None:
        self._old_collor = self._light.color
        self._light.change_color(self._color)

    def undo(self) -> None:
        self._light.change_color(self._old_collor)


class RemoteController:
    """Invoker - Controle Remoto"""

    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}

    def button_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def button_execute(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()

    def button_undo(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()


if __name__ == "__main__":
    bedroon_light = Light('Luz do quarto', 'Quarto')
    living_room_light = Light('Luz da sala', 'Sala')

    bedroon_light_on_command = LightOnCommand(bedroon_light)
    living_room_light_on_command = LightOnCommand(living_room_light)
    living_room_light_change_color_command = LightChangeColor(
        living_room_light, 'verde')
    bedroon_light_change_color_command = LightChangeColor(
        bedroon_light, 'vermelho')

    remote_controller = RemoteController()
    remote_controller.button_add_command(
        'bedroon_light_on', bedroon_light_on_command)
    remote_controller.button_add_command(
        'living_room_light_on', living_room_light_on_command)
    remote_controller.button_add_command(
        'living_room_light_change_color', living_room_light_change_color_command)
    remote_controller.button_add_command(
        'bedroon_light_change_color', bedroon_light_change_color_command)

    remote_controller.button_execute('bedroon_light_on')
    remote_controller.button_execute('living_room_light_on')
    remote_controller.button_undo('bedroon_light_on')
    remote_controller.button_execute('bedroon_light_on')
    remote_controller.button_execute('bedroon_light_on')
    remote_controller.button_execute('bedroon_light_change_color')
    remote_controller.button_execute('living_room_light_change_color')
    remote_controller.button_undo('living_room_light_change_color')
