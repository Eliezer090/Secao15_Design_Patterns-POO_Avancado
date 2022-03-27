

from abc import ABC, abstractmethod


class Abstrata(ABC):
    def template_method(self):
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()

    def base_class_method(self):
        print("base class method")

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    def hook(self):
        pass


class ConcretClass1(Abstrata):
    def hook(self):
        print("hook method Class1")

    def operation1(self):
        print("operation 1 Class1")

    def operation2(self):
        print("operation 2 Class1")


class ConcretClass2(Abstrata):
    def operation1(self):
        print("operation 1 Class2")

    def operation2(self):
        print("operation 2 Class2")


if __name__ == "__main__":
    concret_class1 = ConcretClass1()
    concret_class1.template_method()
    print("\n")
    concret_class2 = ConcretClass2()
    concret_class2.template_method()
