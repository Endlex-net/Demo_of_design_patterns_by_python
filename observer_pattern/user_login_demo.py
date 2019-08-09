import datetime
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


class Account():
    """用户账户"""
    account_infos = {}  # 模拟一个数据库

    def __init__(self, account_id, name, phone, email):
        super().__init__()
        self._latest_ip = None
        self._name = None
        self._email = None
        self._phone = None
        self._account_id = None

        self.account_id = account_id
        self.latest_ip = "0.0.0.0"
        self.name = name
        self.email = email
        self.phone = phone

    @property
    def account_id(self) -> int:
        return self._account_id

    @account_id.setter
    def account_id(self, account_id: int) -> None:
        isinstance(id, int), TypeError(f"id must is str, not {type(account_id)}")
        self._account_id = account_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        isinstance(name, str), TypeError(f"name must is str, not {type(name)}")
        self._name = name

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, phone: str) -> None:
        isinstance(phone, str), TypeError(f"phone must is str, not {type(phone)}")
        self._phone = phone

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email) -> None:
        isinstance(email, str), TypeError(f"email must is str, not {type(email)}")
        self._email = email

    @property
    def latest_ip(self) -> str:
        return self._latest_ip

    @latest_ip.setter
    def latest_ip(self, latest_ip: str) -> None:
        isinstance(latest_ip, str), TypeError(
            f"latest_ip must is str, not {type(latest_ip)}: {latest_ip}"
        )
        self._latest_ip = latest_ip


class AccountServer(Observable):

    def register(self, name, phone, email, ip):
        account_id = len(Account.account_infos.keys()) + 1
        account = Account(account_id, name, phone, email)
        account.latest_ip = ip
        Account.account_infos[account_id] = {
            "name": account.name,
            "phone": account.phone,
            "email": account.email,
            "latest_id": account.latest_ip
        }

        return account_id

    def login(self, account_id, ip):
        """登陆"""
        account_info = Account.account_infos.get(account_id)
        if account_info:
            account = Account(
                account_id,
                account_info["name"],
                account_info["phone"],
                account_info["email"],
            )

            self.notify_observers(
                {
                    "event": "login",
                    "account_info": {
                        "id": account.latest_ip,
                        "name": account.name,
                        "ip": ip,
                        "email": account.email,
                    },
                    "time": datetime.datetime.now(),
                }
            )
            account.latest_ip = ip
            return account
        return None


class LoginSmSSender(Observer):
    """登陆短信发送器"""

    def update(self, observable, object: Any):
        if object['event'] == "login":
            account_info = object["account_info"]
            date = object["time"].strftime("%Y-%m-%d %H:%M:%S")
            email = account_info["email"]
            name = account_info["name"]
            ip = account_info["ip"]
            print(f"[{email}邮件发送] 您的账户:{name}已经登陆, 登陆ip: {ip}, 登陆时间:{date}")


if __name__ == "__main__":
    account_server = AccountServer()
    account_server.add_observer(LoginSmSSender())
    account_id = account_server.register("endlex", "+86 11111111", "endlex@aliyun.com", "127.0.0.1")
    account = account_server.login(account_id, "127.0.0.1")
