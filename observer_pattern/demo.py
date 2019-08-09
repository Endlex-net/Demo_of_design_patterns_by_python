from abc import ABC, abstractmethod
from typing import Any


class Observer(ABC):
    """观察者抽象类"""

    @abstractmethod
    def update(self, observable, object: Any):
        """信息更新抽象方法"""
        pass


class Observable(ABC):
    """被观察者抽象类"""

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer: Observer) -> None:
        """增加观察者"""
        assert isinstance(observer, Observer), TypeError(
            f"observer must is Observer, not {type(observer)}: {observer}"
        )
        self.__observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        """移除观察者"""
        assert isinstance(observer, Observer), TypeError(
            f"observer must is Observer, not {type(observer)}: {observer}"
        )
        self.__observers.remove(observer)

    def notify_observers(self, object: Any = None) -> None:
        """通知观察者"""
        for observer in self.__observers:
            observer.update(self, object)


class WaterHeater(Observable):
    """热水器"""

    def __init__(self):
        super().__init__()
        self.__temperature = None

        self.temperature = 25.0

    @property
    def temperature(self) -> float:
        """温度"""
        return self.__temperature

    @temperature.setter
    def temperature(self, temperature: float) -> None:
        assert isinstance(temperature, float), TypeError(
            f"temperature must is float, not{type(temperature)}: {temperature}"
        )
        self.__temperature = temperature
        print(f"当前温度是: {temperature}C")
        self.notify_observers()


class WashingMode(Observer):
    """洗澡模式"""

    def update(self, water_heater: WaterHeater, object: Any):
        """更新"""
        assert isinstance(water_heater, WaterHeater), TypeError(
            f"water_heater must is WaterHeater, not {type(water_heater)}: {water_heater}"
        )
        if water_heater.temperature >= 50:
            print("水已经热了，可以洗澡了")


class DrinkingMode(Observer):
    """喝水模式"""

    def update(self, water_heater: WaterHeater, object: Any):
        assert isinstance(water_heater, WaterHeater), TypeError(
            f"water_heater must is WaterHeater, not {type(water_heater)}: {water_heater}"
        )
        if water_heater.temperature >= 100:
            print("水已经烧开！可以饮用了")


if __name__ == "__main__":
    water_heater = WaterHeater()
    water_heater.add_observer(WashingMode())
    water_heater.add_observer(DrinkingMode())

    water_heater.temperature = 60.0
    water_heater.temperature = 100.0
