from abc import ABC, abstractmethod


class Request:
    """请求"""


class Handler(ABC):
    """处理者"""

    def __init__(self):
        self.__successor = None

    @property
    def successor(self) -> 'Handler':
        return self.__successor

    def successor(self, successor: 'Handler') -> None:
        assert isinstance(successor, Handler), TypeError(f"successor must is Handler, not {type(successor)}")
        self.__successor = successor

    @abstractmethod
    def handler_request(self, request: Request):
        pass


class OffRequest(Request):
    """请假请求"""

    def __init__(self, name, off_day, reason):
        self.name = name
        self.off_day = off_day
        self.reason = reason


class Manager(Handler):
    def __init__(self, name: str, title: str):
        self.name = name
        self.title = title
        super().__init__()

    def handler_request(self, request: OffRequest):
        raise NotImplementedError


class Supervisor(Manager):
    def handle_request(self, off_request: OffRequest):
        if off_request.off_day <= 2:
            print(f"同意{off_request.name}请假，签字人：{self.title}-{self.name}")

        elif self.successor:
            print(f"{self.title}-{self.name}权限不够，向上提交")
            return self.successor.handle_request(off_request)


class DepartmentManager(Manager):
    def handle_request(self, off_request: OffRequest):
        if off_request.off_day <= 5:
            print(f"同意{off_request.name}请假，签字人：{self.title}-{self.name}")

        elif self.successor:
            print(f"{self.title}-{self.name}权限不够，向上提交")
            return self.successor.handle_request(off_request)


class CEOManager(Manager):
    def handle_request(self, off_request: OffRequest):
        if off_request.off_day <= 20:
            print(f"同意{off_request.name}请假，签字人：{self.title}-{self.name}")

        elif self.successor:
            print(f"{self.title}-{self.name}权限不够，向上提交")
            return self.successor.handle_request(off_request)


class Administrator(Manager):
    def handle_request(self, off_request: OffRequest):
        print(f"同意{off_request.name}请假，签字人：{self.title}-{self.name}")


if __name__ == "__main__":
    direct_leader = Supervisor("Eren", "研发部经理")
    department_leader = DepartmentManager("Eric", "技术研发中心总监")
    ceo = CEOManager("Helen", "CEO")
    administrator = Administrator("Nina", "行政中心总监")

    direct_leader.successor = department_leader
    department_leader.successor = ceo
    ceo.successor = administrator

    sunny_off_reqeust = OffRequest("sunny", 10, "申请旅游")

    direct_leader.handle_request(sunny_off_reqeust)
