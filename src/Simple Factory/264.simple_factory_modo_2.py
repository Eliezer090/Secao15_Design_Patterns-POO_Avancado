
from abc import ABC, abstractmethod
from random import choice


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


class VaiculoFactory:
    def __init__(self, tipo) -> None:
        self.carro = self.get_carro(tipo)
    # Esta aqui seria a simple factory, pois ela faz a comunicação do cliente com a busca.

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        elif tipo == 'popular':
            return CarroPopular()
        elif tipo == 'moto':
            return Moto()
        else:
            raise ValueError('Tipo de veiculo inválido')

    def buscar_cliente(self) -> None:
        self.carro.buscar_cliente()


if __name__ == '__main__':
    carros_disponiveis = ['luxo', 'popular', 'moto']

    for i in range(10):
        carro = VaiculoFactory(choice(carros_disponiveis))
        carro.buscar_cliente()
