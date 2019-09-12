from abc import ABC, abstractmethod


class Builder(ABC):

    @abstractmethod
    def get_result(self):
        pass


class CarBuilder(Builder):
    def __init__(self):
        self.car = Car('一个玩具小车')

    def set_wheel(self):
        self.car.add_component("轮子", 4)

    def set_body(self):
        self.car.add_component("车身", 1)

    def set_engine(self):
        self.car.add_component("发动机", 1)

    def set_steering_wheel(self):
        self.car.add_component("方向盘", 1)

    def get_result(self):
        return self.car


class Product:
    """产品类"""
    pass


class Car(Product):
    """小车"""

    def __init__(self, name):
        self.name = name
        self.__component = []

    def add_component(self, component, count=1, unit="个"):
        self.__component.append([component, count, unit])
        print(f"{self.name}增加了{count}{unit}{component}")

    def feature(self):
        print(f"我是{self.name}, 我可以快速奔跑...")


class Director:
    """指挥者"""

    @staticmethod
    def construct(car_builder: CarBuilder):
        car_builder.set_body()
        car_builder.set_wheel()
        car_builder.set_steering_wheel()
        car_builder.set_engine()
        return car_builder.get_result()


if __name__ == "__main__":
    car = Director.construct(CarBuilder())
    car.feature()
