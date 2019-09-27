from abc import ABC, abstractmethod


class Chef:
    """厨师"""

    def steam_food(self, original_material):
        """清蒸食物"""
        print(f"{original_material}清蒸中...")
        return "清蒸" + original_material

    def stir_friend_food(self, original_material):
        """爆炒食物"""
        print(f"{original_material}爆炒中...")
        return "爆炒" + original_material


class Order(ABC):
    """订单"""

    def __init__(self, name, original_material):
        self._chef = Chef()
        self._name = name
        self._original_material = original_material

    def get_display_name(self):
        return self._name + self._original_material

    @abstractmethod
    def processing_order(self):
        pass


class SteamedOrder(Order):
    """清蒸"""

    def __init__(self, original_material):
        super().__init__("清蒸", original_material)

    def processing_order(self):
        if self._chef:
            return self._chef.steam_food(self._original_material)
        return ""


class SpicyOrder(Order):
    """香辣炒"""

    def __init__(self, original_material):
        super().__init__("香辣炒", original_material)

    def processing_order(self):
        if self._chef:
            return self._chef.stir_friend_food(self._original_material)


class Waiter:
    """服务员"""

    def __init__(self, name):
        self.__name = name
        self.__order = None

    def receive_order(self, order: Order):
        self.__order = order
        print(f"服务员{self.__name}: 您的{order.get_display_name()}已经收到，请耐心等待")

    def place_order(self):
        food = self.__order.processing_order()
        print(f"服务员{self.__name}： 您点的{food}已经准备好，请慢用")


if __name__ == "__main__":
    waiter = Waiter("Endlex")
    steamed_order = SteamedOrder("大闸蟹")
    print(f"客户Clay:我要一份{steamed_order.get_display_name()}")
    waiter.receive_order(steamed_order)
    waiter.place_order()
