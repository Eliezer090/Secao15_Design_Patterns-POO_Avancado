"""
    Composite é um padrão de projeto que é representado pela estrutura de arvore, ele tem por objetivo
        agrupar objetos em um único objeto:
                  11
            7           15
        5       9   13      20
    Um exemplo de composite é quando vc compra produtos em uma loja, os produtos seriam os 'leafs/objetos', e o
        composite seria a caixa que agrupa os produtos, mas este composite pode ser colocado dentro de outros
        composites, com isso temos uma hierarquia de composites, como no exemplo acima, e inclusive é o exemplo abaixo.
    
    A caixa é o composite e o leaf é o/s produtos.
Aplicabilidae:
    No mundo real seria em uma transportadora, onde tem o caminhão, que tem palets e cada palet tem as caixas
        de produtos, e cada caixa tem os produtos, que pode haver outras caixas dentro, e assim por diante.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class IBoxStructure(ABC):
    """Component"""
    @abstractmethod
    def print_content(self) -> None:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

    def add(self, box: IBoxStructure) -> None:
        pass

    def remove(self, box: IBoxStructure) -> None:
        pass


class Box(IBoxStructure):
    """Composite"""

    def __init__(self, name: str) -> None:
        self._name: str = name
        self._children: List[IBoxStructure] = []

    def print_content(self) -> None:
        print('')
        print('NOVA CAIXA')  # Só exibe 'NOVA CAIXA' para as caixas
        Product(self._name, self.get_price()).print_content()

        for child in self._children:
            # Só exibe 'PRODUTO' para os produtos, quando acaba os produtos ele vai para a proxima caixa e volta para o 'NOVA CAIXA'
            print('PRODUTO')
            #Product(self._name, self.get_price()).print_content()
            child.print_content()

    def get_price(self) -> float:
        return sum([child.get_price() for child in self._children])

    def add(self, box: IBoxStructure) -> None:
        self._children.append(box)

    def remove(self, box: IBoxStructure) -> None:
        if box in self._children:
            self._children.remove(box)

    def __str__(self) -> str:
        return '{}'.format(self._name)


class Product(IBoxStructure):
    """Leaf"""

    def __init__(self, name: str, price: float) -> None:
        self._name: str = name
        self._price: float = price

    def print_content(self) -> None:
        print(f'{self._name} - {self._price}')

    def get_price(self) -> float:
        return self._price


if __name__ == "__main__":
    camiseta1 = Product('Camiseta 1 NIKE', 10)
    camiseta2 = Product('Camiseta 2 NIKE', 20)
    camiseta3 = Product('Camiseta 3 NIKE', 30)
    camiseta4 = Product('Camiseta 4 ADIDAS', 40)
    camiseta5 = Product('Camiseta 5 ADIDAS', 50)

    caixa1 = Box('Caixa Camisetas - NIKE')
    caixa1.add(camiseta1)
    caixa1.add(camiseta2)
    caixa1.add(camiseta3)

    # Dependendo da forma que add a caixa ela é exibida antes ou depois das camisas
    caixa2 = Box('Caixa camisetas - ADIDAS')
    # caixa2.add(caixa1)
    caixa2.add(camiseta4)
    caixa2.add(camiseta5)
    # caixa2.add(caixa1)

    caixa3 = Box('Caixa Camisetas')
    caixa3.add(caixa1)
    caixa3.add(caixa2)

    smartphone1 = Product('Smartphone 1 iphone', 1000)
    smartphone2 = Product('Smartphone 2 iphone', 2000)
    smartphone3 = Product('Smartphone 3 iphone', 3000)

    caixa4 = Box('Caixa Smartphones')
    caixa4.add(smartphone1)
    caixa4.add(smartphone2)
    caixa4.add(smartphone3)

    caixa5 = Box('Caixa Produtos')
    caixa5.add(caixa3)
    caixa5.add(caixa4)

    caixa5.print_content()


"""
Abaixo está representado a arvore:
                                       Caixa Produtos
                    Caixa Camisetas         |           Caixa Smartphones
            ADIDAS        |       NIKE      |               Smartphone 1 iphone - 1000
             4            |        1        |               Smartphone 2 iphone - 2000
             5            |        2        |               Smartphone 3 iphone - 3000
                          |        3        |

A saida:
NOVA CAIXA
Caixa Produtos - 6150
PRODUTO

NOVA CAIXA
Caixa Camisetas - 150
PRODUTO

NOVA CAIXA
Caixa Camisetas - NIKE - 60
PRODUTO
Camiseta 1 NIKE - 10
PRODUTO
Camiseta 2 NIKE - 20
PRODUTO
Camiseta 3 NIKE - 30
PRODUTO

NOVA CAIXA
Caixa camisetas - ADIDAS - 90
PRODUTO
Camiseta 4 ADIDAS - 40
PRODUTO
Camiseta 5 ADIDAS - 50
PRODUTO

NOVA CAIXA
Caixa Smartphones - 6000
PRODUTO
Smartphone 1 iphone - 1000
PRODUTO
Smartphone 2 iphone - 2000
PRODUTO
Smartphone 3 iphone - 3000

"""
