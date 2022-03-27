"""
    Observar a ordem de execução dos prints.
"""


class Meta(type):
    def __call__(self, *args, **kwds):
        print('Call Meta')
        return super().__call__(*args, **kwds)


class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwds):
        print('new é executado ')
        return super().__new__(cls)

    def __init__(self, nome) -> None:
        print('init é executado')
        self.nome = nome

    def __call__(self, x, y):
        print('call Pessoa')
        print('Chamando Pessoa', self.nome, x+y)


p1 = Pessoa('João')
p1(2, 2)
print(p1.nome)
