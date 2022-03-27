"""
    Exemplo de um radio de carro, os mesmos 2 botões em diferentes modos podem exercer funções diferentes.
    Função:
        Radio:
            BTN_Next:
                Passa para a próxima extação de radio.
            BTN_Prev
                Passa para a extação anterior de radio.
        CD/Music:
            BTN_Next:
                Passa para a próxima faixa de música.
            BTN_Prev:
                Passa para a faixa anterior de música.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Sound:
    def __init__(self) -> None:
        self.mode: PlayMode = RadioMode(self)
        self.playing: int = 0

    def pess_next(self) -> None:
        print("Tentando executar pess_next() no modo: ", self.mode)
        self.mode.press_next()
        print("\n")

    def pess_prev(self) -> None:
        print("Tentando executar pess_prev() no modo: ", self.mode)
        self.mode.press_previous()
        print("\n")

    def pess_change_mode(self) -> None:
        print("Tentando executar pess_change_mode() modo atual: ", self.mode)
        self.mode.change_mode()

    def microphone_mode(self) -> None:
        print("Tentando executar microphone_mode() modo atual: ", self.mode)
        self.mode.microphone_mode()
        print("\n")


class PlayMode(ABC):
    def __init__(self, sound: Sound) -> None:
        self.sound = sound

    @abstractmethod
    def press_next(self) -> None:
        pass

    @abstractmethod
    def press_previous(self) -> None:
        pass

    @abstractmethod
    def change_mode(self) -> None:
        pass

    def microphone_mode(self) -> None:
        pass

    def __str__(self) -> str:
        return self.__class__.__name__


class RadioMode(PlayMode):
    def press_next(self) -> None:
        self.sound.playing += 1000
        print("Playing Station: ", self.sound.playing)

    def press_previous(self) -> None:
        self.sound.playing -= 1000 if self.sound.playing > 0 else 0
        print("Playing Station: ", self.sound.playing)

    def change_mode(self) -> None:
        self.sound.mode = MusicMode(self.sound)
        self.sound.playing = 1


class MusicMode(PlayMode):
    def press_next(self) -> None:
        self.sound.playing += 1
        print("Playing Track: ", self.sound.playing)

    def press_previous(self) -> None:
        self.sound.playing -= 1 if self.sound.playing > 0 else 0
        print("Playing Track: ", self.sound.playing)

    def change_mode(self) -> None:
        self.sound.mode = CableMode(self.sound)
        self.sound.playing = 1


class CableMode(PlayMode):
    def press_next(self) -> None:
        self.sound.playing += 20
        print("Playing Cable Track: ", self.sound.playing)

    def press_previous(self) -> None:
        self.sound.playing -= 20 if self.sound.playing > 0 else 0
        print("Playing Cable Track: ", self.sound.playing)

    def change_mode(self) -> None:
        self.sound.mode = RadioMode(self.sound)
        self.sound.playing = 1000

    def microphone_mode(self) -> None:
        print("Microphone Mode")


if __name__ == "__main__":
    sound = Sound()
    sound.pess_next()
    sound.pess_prev()
    sound.pess_change_mode()
    sound.pess_next()
    sound.pess_next()
    sound.pess_next()
    sound.pess_prev()
    sound.pess_change_mode()
    sound.microphone_mode()
    sound.pess_next()
    sound.pess_next()
    sound.pess_next()
    sound.pess_next()
    sound.pess_next()
    sound.pess_next()
    sound.pess_prev()
    sound.pess_change_mode()
    sound.pess_next()
    sound.pess_next()
    sound.pess_next()
    sound.pess_next()
    sound.pess_prev()
    sound.pess_prev()
    sound.pess_prev()
    sound.pess_change_mode()
    sound.pess_next()
