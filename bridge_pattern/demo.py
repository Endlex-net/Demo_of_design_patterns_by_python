from abc import ABC, abstractmethod


class Implementor(ABC):

    @abstractmethod
    def operation(self):
        pass


class ConcreteImplementorA(Implementor):
    def operation(self):
        print("plan A")


class ConcreteImplementorB(Implementor):
    def operation(self):
        print("plan B")


class Abstraction(object):

    def __init__(self, implementor: Implementor = None):
        if not implementor:
            self.__implementor = implementor

    @property
    def implementor(self):
        return self.__implementor

    @implementor.setter
    def implementor(self, implementor: Implementor):
        assert isinstance(implementor, Implementor), TypeError("implementor must is Implementor")
        self.__implementor = implementor

    def operation(self):
        return self.__implementor.operation()


class RefinedAbstraction(Abstraction):
    pass


if __name__ == "__main__":
    ab = RefinedAbstraction()
    ab.implementor = ConcreteImplementorA()
    ab.operation()

    ab.implementor = ConcreteImplementorB()
    ab.operation()
