from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self) -> None:
        self.sucessor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str:
        pass


class HandlerABC(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters = ['A', 'B', 'C']
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return 'HandlerABC consegiu tratar o valor: ' + letter
        return self.sucessor.handle(letter)


class HandlerDEF(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters = ['D', 'E', 'F']
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return 'HandlerDEF consegiu tratar o valor: ' + letter
        return self.sucessor.handle(letter)


class HandlerUnsolved(Handler):
    def handle(self, letter: str) -> str:
        return 'HandlerUnsolved não consegiu tratar o valor: ' + letter


if __name__ == "__main__":
    handlers = HandlerABC(HandlerDEF(HandlerUnsolved()))
    print(handlers.handle('A'))
    print(handlers.handle('B'))
    print(handlers.handle('E'))
    print(handlers.handle('F'))
    print(handlers.handle('N'))
