
class StringReprMixing:
    def __str__(self):
        parms = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])

        return f'{self.__class__.__name__}({parms})'

    def __repr__(self) -> str:
        return self.__str__()


"""EXEMPLOS
class A(StringReprMixing):
    def __init__(self, nome):
        self.x = 1
        self.y = 2
        self.z = 3
        self.nome = nome


a = A('nome')
# print(a.__dict__)
print(a)
"""
# Monostate


class MonoStateSimple(StringReprMixing):
    _state: dict = {
        'x': 10,
        'y': 20,
    }

    def __init__(self, nome=None, sobrenome=None) -> None:
        self.__dict__ = self._state
        self.x: str = ''
        if nome is not None:
            self.nome = nome
        if sobrenome is not None:
            self.sobrenome = sobrenome


if __name__ == '__main__':
    # impacta nas 2 instancias
    m1 = MonoStateSimple('Eliézer')
    m2 = MonoStateSimple()
    m1.x = 'Qualquer coisa'
    print(m1)
    print(m2)
