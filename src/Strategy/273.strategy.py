
"""
    Estratégias, em um contexto de desconto de preço de produtos, maximo que o vendedor 
        pode dar baseado no produto X poe exemplo.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    def __init__(self, total: float, discount: DiscountStrategy) -> None:
        self._total = total
        self._discount = discount

    @property
    def total(self) -> float:
        return self._total

    @property
    def total_with_discount(self) -> float:
        return self._discount.calculate(self._total)


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float:
        pass


class TwentyPercentDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)


class FivePercentDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value


class CustomDiscount(DiscountStrategy):
    def __init__(self, discount: float) -> None:
        self._discount = discount / 100

    def calculate(self, value: float) -> float:
        return value - (value * self._discount)


if __name__ == '__main__':
    order = Order(1000, TwentyPercentDiscount())
    print(order.total_with_discount)
    order = Order(1000, FivePercentDiscount())
    print(order.total_with_discount)

    order = Order(1000, NoDiscount())
    print(order.total_with_discount)

    order = Order(1000, CustomDiscount(5))
    print(order.total_with_discount)
