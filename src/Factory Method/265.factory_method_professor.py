
from abc import ABC, abstractmethod
from random import choice

"""
    A explicação do professor para fazer assim é que cada Zona(Filial) pode realizar implementações
      independentes de outras filiais, mas se verificar temos códigos duplicados o que vai contra o 
      padrão de POO, pois se um dia mudar o nome de alguma class implentada terá que mudar em todos os locais.
"""


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('CarroLuxo Buscando cliente')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('CarroPopular Buscando cliente')


class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto Buscando cliente')


class VaiculoFactory():
    def __init__(self, tipo) -> None:
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo:
        pass

    def buscar_cliente(self) -> None:
        self.carro.buscar_cliente()


class ZonaNorteVeiculos(VaiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        elif tipo == 'popular':
            return CarroPopular()
        elif tipo == 'moto':
            return Moto()
        else:
            assert 0, 'Tipo de veiculo inválido'


class ZonaSulVeiculos(VaiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'popular':
            return CarroPopular()
        else:
            raise ValueError('Tipo de veiculo inválido')


if __name__ == '__main__':
    veiculos_disponiveis_Zona_Norte = ['luxo', 'popular', 'moto']
    veiculos_disponiveis_Zona_Sul = ['popular', 'moto']
    for i in range(10):
        carro = ZonaNorteVeiculos(choice(veiculos_disponiveis_Zona_Norte))
        carro.buscar_cliente()

    print('\n')
    for i in range(10):
        carro_sul = ZonaSulVeiculos(choice(veiculos_disponiveis_Zona_Sul))
        carro_sul.buscar_cliente()
