from abc import ABC, abstractmethod


class Car(ABC):
    """Product"""

    @abstractmethod
    def show(self):
        pass


class FerrariCar(Car):
    """法拉利"""

    def show(self):
        print(f'这辆车是辆法拉利')


class BenzCar(Car):
    """奔驰车"""

    def show(self):
        print(f"这辆车是一辆奔驰")


class CarFactory(ABC):
    """Creator"""

    @abstractmethod
    def create(self) -> Car:
        pass


class FerrariCarFactory(CarFactory):
    """法拉利工厂"""

    def create(self) -> FerrariCar:
        return FerrariCar()


class BenzCarFactory(CarFactory):
    """奔驰车工厂"""

    def create(self) -> BenzCar:
        return BenzCar()


if __name__ == "__main__":
    benz_car_factory = BenzCarFactory()
    benz_car = benz_car_factory.create()
    benz_car.show()

    ferrari_car_factory = FerrariCarFactory()
    ferrari_car = ferrari_car_factory.create()
    ferrari_car.show()
