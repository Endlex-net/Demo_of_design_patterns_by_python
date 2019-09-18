from abc import ABC, abstractmethod


class Car(ABC):
    """Product"""

    @abstractmethod
    def show(self):
        pass


class FerrariCar(Car):
    """法拉利车抽象类"""

    def __init__(self):
        self.origin_place = "未知产地的"

    def show(self):
        print(f"这是一辆{self.origin_place}法拉利")


class DomesticFerrariCar(FerrariCar):
    """国产法拉利"""

    def __init__(self):
        super().__init__()
        self.origin_place = "国产"


class ImportFerrariCar(FerrariCar):
    """进口法拉利"""

    def __init__(self):
        super().__init__()
        self.origin_place = "进口"


class BenzCar(Car):
    """法拉利车抽象类"""

    def __init__(self):
        self.origin_place = "未知产地的"

    def show(self):
        print(f"这是一辆{self.origin_place}奔驰")


class DomesticBenzCar(FerrariCar):
    """国产法奔驰"""

    def __init__(self):
        super().__init__()
        self.origin_place = "国产"


class ImportBenzCar(FerrariCar):
    """进口法奔驰"""

    def __init__(self):
        super().__init__()
        self.origin_place = "进口"


class CarFactory(ABC):
    """Creator"""

    @abstractmethod
    def create_ferrari_car(self):
        pass

    @abstractmethod
    def create_benz_car(self):
        pass


class DomesticCarFactory(CarFactory):
    """国内车工厂"""

    def create_benz_car(self):
        return DomesticBenzCar()

    def create_ferrari_car(self):
        return DomesticFerrariCar()


class ImportCarFactory(CarFactory):
    """原厂车工厂"""

    def create_ferrari_car(self):
        return ImportFerrariCar()

    def create_benz_car(self):
        return ImportBenzCar()


if __name__ == "__main__":
    domestic_car_factory = DomesticCarFactory()
    benz_car = domestic_car_factory.create_benz_car()
    benz_car.show()
    ferrari_car = domestic_car_factory.create_ferrari_car()
    ferrari_car.show()

    import_car_factory = ImportCarFactory()
    benz_car = import_car_factory.create_benz_car()
    benz_car.show()
    ferrari_car = import_car_factory.create_ferrari_car()
    ferrari_car.show()
