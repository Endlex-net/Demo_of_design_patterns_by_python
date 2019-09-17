from abc import ABC, abstractmethod


class Target:
    pass


class Adapher:
    pass


class Adaptee:
    pass


class SocketEntity:
    """接口实体抽象定义"""

    def __init__(self, pin_num, pin_type):
        self.__pin_num = None
        self.__pin_type = None

        self.pin_num = pin_num
        self.pin_type = pin_type

    @property
    def pin_num(self):
        return self.__pin_num

    @pin_num.setter
    def pin_num(self, pin_num):
        self.__pin_num = pin_num

    @property
    def pin_type(self):
        return self.__pin_type

    @pin_type.setter
    def pin_type(self, pin_type):
        self.__pin_type = pin_type


class ISocket:
    """插座类型抽象类"""

    def __init__(self):
        self.name = None
        self.socket = None


class ChineseSocket(ISocket, Target):
    """中国插头"""

    def __init__(self):
        super().__init__()
        self.name = "中国插头"
        self.socket = SocketEntity(3, "八字扁平")


class BritishSocket(ISocket, Adaptee):
    """英国插头"""

    def __init__(self):
        super().__init__()
        self.name = "英标插头"
        self.socket = SocketEntity(3, "T字方形")


class AdapterSocket(ChineseSocket, Adapher):
    """插座转换器"""

    def __init__(self, british_socket: BritishSocket):
        self.__british_socket = british_socket
        self.socket = SocketEntity(3, '八字扁平')

    @property
    def name(self):
        return self.__british_socket.name + "转换器"


def can_charge_for_digtal_device(some_socket: ISocket):
    if some_socket.socket.pin_num == 3 and some_socket.socket.pin_type == "八字扁平":
        can_charge = "可以"

    else:
        can_charge = "不可以"

    print(
        f"{some_socket.name}: {some_socket.socket.pin_num}脚针, {some_socket.socket.pin_type}, {can_charge}给中国设备充电")


if __name__ == "__main__":
    chinese_socket = ChineseSocket()
    can_charge_for_digtal_device(chinese_socket)

    british_socket = BritishSocket()
    can_charge_for_digtal_device(british_socket)

    adapter_socket = AdapterSocket(british_socket)
    can_charge_for_digtal_device(adapter_socket)
