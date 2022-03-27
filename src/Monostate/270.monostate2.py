
class StringReprMixing:
    def __str__(self):
        parms = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])

        return f'{self.__class__.__name__}({parms})'

    def __repr__(self) -> str:
        return self.__str__()


class MonoStateNew(StringReprMixing):
    _state: dict = {
        'x': 10,
        'y': 20,
    }

    def __new__(cls, *args, **kwds):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, nome=None, sobrenome=None) -> None:

        if nome is not None:
            self.nome = nome
        if sobrenome is not None:
            self.sobrenome = sobrenome


class A(MonoStateNew):
    pass


if __name__ == '__main__':
    # impacta nas 2 instancias
    m1 = MonoStateNew(nome='Eliézer')
    m2 = MonoStateNew(sobrenome='Santos')
    m3 = A(nome='Pedro')
    m1.x = 'Qualquer coisa'
    print(m1)
    print(m2)
