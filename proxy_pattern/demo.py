from abc import ABC, abstractmethod


class Subject(ABC):
    """主题类"""

    @abstractmethod
    def request(self):
        pass


class RealSubject(Subject):

    def request(self):
        raise NotImplementedError


class ProxySubject(Subject):

    def request(self):
        raise NotImplementedError


class TonyReception(RealSubject):
    def __init__(self, name, phone_number):
        self.phone_number = phone_number
        self.name = name

    def request(self, parcel_content):
        print(f"货物主任:{self.name}, 手机号: {self.phone_number}")
        print(f"接收到一个包裹，包裹内容是: {parcel_content}")


class WendyReception(ProxySubject):
    """Wendy代收"""

    def __init__(self, name, receiver: TonyReception):
        self.name = name
        self.receiver: TonyReception = receiver

    def request(self, parcel_content):
        print(f"我是{self.receiver.name} 的朋友， 我来帮他代收快递!")
        if self.receiver:
            self.receiver.request(parcel_content)
        print(f"代收人: {self.name}")


if __name__ == "__main__":
    tony = TonyReception("Tony", "123424")
    print("Tony接收:")
    tony.request("雪地靴")
    print()

    print("Wendy代收:")
    wendy = WendyReception("Wendy", tony)
    wendy.request("雪地靴")
