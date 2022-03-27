
from abc import ABC, abstractmethod
from random import choice


class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('CarroLuxo ZN Buscando cliente')


class CarroLuxoZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('CarroLuxo ZN Buscando cliente')


class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular ZN Buscando cliente')


class MotoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto ZS Buscando cliente')


class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('CarroPopular ZS Buscando cliente')


class MotoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto ZS Buscando cliente')


class MotoPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto popular ZS Buscando cliente')


class VaiculoFactory():
    @staticmethod
    @abstractmethod
    def get_carro_luxo(tipo: str) -> VeiculoLuxo:
        pass

    @staticmethod
    @abstractmethod
    def get_carro_popular(tipo: str) -> VeiculoPopular:
        pass

    @staticmethod
    @abstractmethod
    def get_moto_luxo(tipo: str) -> VeiculoLuxo:
        pass

    @staticmethod
    @abstractmethod
    def get_moto_popular(tipo: str) -> VeiculoPopular:
        pass


class ZonaNorteVeiculos(VaiculoFactory):
    @staticmethod
    def get_carro_luxo(tipo: str) -> VeiculoLuxo:
        return CarroLuxoZN()

    @staticmethod
    def get_carro_popular(tipo: str) -> VeiculoPopular:
        return CarroPopularZN()

    @staticmethod
    def get_moto_luxo(tipo: str) -> VeiculoLuxo:
        return MotoZN()


class ZonaSulVeiculos(VaiculoFactory):
    @staticmethod
    def get_carro_popular(tipo: str) -> VeiculoPopular:
        return CarroPopularZS()

    @staticmethod
    def get_moto_luxo(tipo: str) -> VeiculoLuxo:
        return MotoZS()

    @staticmethod
    def get_moto_popular(tipo: str) -> VeiculoPopular:
        return MotoPopularZS()


class Cliente:
    def busca_cliente(self):
        for factory in [ZonaNorteVeiculos(), ZonaSulVeiculos()]:

            carro_popular = factory.get_carro_popular(
                choice(['popular', 'luxo']))
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo(choice(['luxo', 'popular']))
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular(
                choice(['popular', 'luxo']))
            moto_popular.buscar_cliente()
            moto_luxo = factory.get_moto_luxo(choice(['luxo', 'popular']))
            moto_luxo.buscar_cliente()


if __name__ == '__main__':
    cliente = Cliente()
    cliente.busca_cliente()
