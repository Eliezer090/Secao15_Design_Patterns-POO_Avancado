
"""
    Decocarodor de classes, mas a execução é a classe que faz e nao o decorador. Um exemplo seria roupas
        ou seja, quando esta frio voce coloca mais e mais roupas, voce está se decorando mas o componente 
        seria voce.
    Exemplo abaixo é um caso de uma lanchonete, com decorator generico onde pode ser adicionado qualquer 
        ingrediente a mais em qualquer lanche e o preço dele é incrementado.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from copy import deepcopy
from dataclasses import dataclass
from typing import List

# Ingridients


@dataclass
class Ingredient:
    price: float


@dataclass
class Bread(Ingredient):
    price: float = 1.50


@dataclass
class Sausage(Ingredient):
    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    price: float = 7.99


@dataclass
class Egg(Ingredient):
    price: float = 1.50


@dataclass
class Cheese(Ingredient):
    price: float = 6.35


@dataclass
class MashedPotatoes(Ingredient):
    price: float = 2.50


@dataclass
class PotatoSticks(Ingredient):
    price: float = 2.50


# Hot Dogs
class HotDog:
    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([ingredient.price for ingredient in self._ingredients]), 2)

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        return f"{self.name} - {self.price} -> {self.ingredients}"


class SimpleHotDog(HotDog):
    def __init__(self) -> None:
        self._name = "Simple Hot Dog"
        self._ingredients: List[Ingredient] = [
            Bread(), Sausage(), PotatoSticks()]


class SpecialHotDog(HotDog):
    def __init__(self) -> None:
        self._name = "Special Hot Dog"
        self._ingredients: List[Ingredient] = [
            Bread(), Sausage(), Bacon(), Egg(), Cheese(), MashedPotatoes(), PotatoSticks()]

# Decorators


class HotDogDecorator(HotDog):
    def __init__(self, hotdog: HotDog, ingredient: Ingredient) -> None:
        self._hotdog = hotdog
        self._ingredient = ingredient
        self._ingredients = deepcopy(hotdog.ingredients)
        self._ingredients.append(ingredient)

    @property
    def name(self) -> str:
        return f"{self._hotdog.name} with {self._ingredient.__class__.__name__}"


if __name__ == "__main__":
    simple_hotdog = SimpleHotDog()
    print(simple_hotdog)
    bacon_simple_hotdog = HotDogDecorator(simple_hotdog, Bacon())
    print(bacon_simple_hotdog)
    cheese_withBacon_simple_hotdog = HotDogDecorator(
        bacon_simple_hotdog, Cheese())
    print(cheese_withBacon_simple_hotdog)
