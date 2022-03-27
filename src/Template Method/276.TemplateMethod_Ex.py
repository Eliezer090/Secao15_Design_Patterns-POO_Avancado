
from abc import ABC, abstractmethod


class Pizza(ABC):
    """Class Abstrata"""

    def prepare(self) -> None:
        """Template Method"""
        self.hook_before_add_ingredients()
        self.add_ingredients()
        self.hook_afther_add_ingredients()
        self.cook()
        self.cut()
        self.serve()

    def hook_before_add_ingredients(self) -> None:
        pass

    def hook_afther_add_ingredients(self) -> None:
        pass

    @abstractmethod
    def add_ingredients(self) -> None:
        pass

    @abstractmethod
    def cook(self) -> None:
        pass

    def cut(self) -> None:
        print("Cutting the pizza {}".format(self.__class__.__name__))

    def serve(self) -> None:
        print("Serving the pizza {}".format(self.__class__.__name__))


class Pizza1(Pizza):

    def hook_before_add_ingredients(self) -> None:
        print("To whash ingredients for pizza1")

    def add_ingredients(self) -> None:
        print("Adding ingredients pizza1 - Tomato, Cheese, Pineapple")

    def cook(self) -> None:
        print("Cooking the pizza pizza1 for 5 minutes")


class Pizza2(Pizza):
    def add_ingredients(self) -> None:
        print("Adding ingredients pizza2 - pepperoni, cheese, mushrooms")

    def cook(self) -> None:
        print("Cooking the pizza pizza2 for 10 minutes")


if __name__ == "__main__":
    pizza1 = Pizza1()
    pizza1.prepare()
    print("\n")
    pizza2 = Pizza2()
    pizza2.prepare()
    print("\n")
