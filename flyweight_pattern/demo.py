from abc import ABC, abstractmethod


class Flyweight(ABC):
    """享元类"""

    @abstractmethod
    def operation(self, extrinsic_state):
        pass


class FlyweightImpl(Flyweight):
    """享元类的具体实现类"""

    def __init__(self, color):
        self.__color = color

    def operation(self, extrinsic_state):
        print(f"{extrinsic_state} 取得{self.__color}")


class FlyweightFactory:
    """享元工厂"""

    def __init__(self):
        self.__flyweights = {}

    def get_flyweight(self, key):
        if key not in self.__flyweights:
            self.__flyweights[key] = FlyweightImpl(key)
        return self.__flyweights[key]


if __name__ == "__main__":
    factory = FlyweightFactory()

    red = factory.get_flyweight("红")
    red.operation("梦之队")

    red2 = factory.get_flyweight("红")
    red.operation("朝阳队")

    print(red is red2)
