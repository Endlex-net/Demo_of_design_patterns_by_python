from abc import ABC, abstractmethod


class Context(ABC):
    """状态模式的抽象环境类"""

    def __init__(self):
        self.__states = []
        self.__state = None

    @property
    def state(self) -> "State":
        return self.__state

    @state.setter
    def state(self, state: "State") -> None:
        self.__state = state

    def add_state(self, state: "State") -> None:
        """添加状态"""
        assert isinstance(state, State), TypeError(f"state must is State, not {type(state)}")
        if state not in self.__states:
            self.__states.append(state)

    def change_state(self) -> None:
        for state in self.__states:
            if state.is_match(self):
                self.state = state


class State(ABC):
    """状态抽象类"""

    def __init__(self, name):
        self.__name = None

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        assert isinstance(name, str), TypeError(f"name must is str, not {type(name)}")
        self.__name = name

    @abstractmethod
    def behavior(self, water: "Water"):
        """不同状态下的行为(抽象方法)"""
        pass

    @abstractmethod
    def is_match(self, context: Context) -> bool:
        pass


class SolidState(State):
    """固态"""

    def __init__(self, name: str):
        super().__init__(name)

    def behavior(self, water: "Water"):
        print(f"我是冰，十分冷，当前温度是{water.temperature}度")

    def is_match(self, context: Context) -> bool:
        if context.temperature and context.temperature <= 0:
            return True


class LiquidState(State):
    """液态"""

    def __init__(self, name: str):
        super().__init__(name)

    def behavior(self, water: "Water"):
        print(f"我是水, 可以流动，当前温度是{water.temperature}度")

    def is_match(self, context: Context) -> bool:
        if context.temperature and 0 < context.temperature < 100:
            return True


class GaseousState(State):
    """气态"""

    def __init__(self, name: str):
        super().__init__(name)

    def behavior(self, water: "Water"):
        print(f"我是蒸汽，我飘在空中, 当前的温度是{water.temperature}度")

    def is_match(self, context: Context) -> bool:
        if context.temperature and context.temperature >= 100:
            return True


class Water(Context):
    """水"""

    def __init__(self):
        super().__init__()
        self.__temperature = None

        self.add_state(SolidState("冰"))
        self.add_state(LiquidState("水"))
        self.add_state(GaseousState("水蒸气气"))
        self.temperature = 25.0

    @property
    def temperature(self) -> float:
        return self.__temperature

    @temperature.setter
    def temperature(self, temperature: float) -> None:
        assert isinstance(temperature, (float, int)), TypeError(
            f'temperature must is float or int, not {type(temperature)}')
        self.__temperature = float(temperature)
        self.change_state()

    def behavior(self):
        self.state.behavior(self)


if __name__ == "__main__":
    water = Water()
    water.temperature = 70
    water.behavior()
    water.temperature = 100
    water.behavior()
    water.temperature = -10
    water.behavior()
