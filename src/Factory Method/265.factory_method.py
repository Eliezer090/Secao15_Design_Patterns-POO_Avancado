
from abc import ABC, abstractmethod
from random import choice

"""
    Desta maneira eu tenho uma class só com todos os tipos de veiculos aceitos, padronizando os carros aceitos
      mas teriamos que ter um outro nivel de controle para saberde qual filial está vindo o pedido, e quais 
      veiculos a filial tem disponivel, mas isso poderia ser parametrizado por exemplo:
        filial  veiculos
        1       popular 
        1       luxo
        1       moto
        2       popular
      O que defini acima poderia ser controlado por parametros ou por um banco de dados, assim se o pedido fosse
        moto na filial 2 iria retornar 'Tipo de veiculo inválido', que foi o que implementei abaixo, deve ter 
        formas melhores de fazer validações, mas a ideia apresentada abaixo acredito que se adaptaria melhor a 
        realidade.
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


class VeiculosDisponiveis():
    @staticmethod
    def veiculos_filial(filial: int) -> list:
        # Aqui seria navegado na BD para buscar os veiculos disponiveis para a filial
        if filial == 1:
            return ['popular', 'luxo', 'moto']
        elif filial == 2:
            return ['popular']
        else:
            raise ValueError('Filial inválida')


class VeiculoFactory():
    def __init__(self, tipo, filial) -> None:
        self.valid = False
        if tipo in VeiculosDisponiveis.veiculos_filial(filial):
            self.carro = self.get_carro(tipo)
            self.valid = True
        else:
            print('Tipo de veiculo "{}" inválido, para a filial {}'.format(tipo, filial))

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
        if self.valid:
            self.carro.buscar_cliente()


if __name__ == '__main__':
    # Estou querendo os tipo de veiculos definidos abaixo, para cada filial
    veiculos_filial_1 = ['luxo', 'popular', 'moto', 'A']
    veiculos_filial_2 = ['popular', 'moto']

    for i in range(10):
        carro = VeiculoFactory(choice(veiculos_filial_1), 1)
        carro.buscar_cliente()

    print('\n')
    for i in range(10):
        carro_sul = VeiculoFactory(choice(veiculos_filial_2), 2)
        carro_sul.buscar_cliente()
