from abc import ABC, abstractmethod


class Memento:
    """备忘录"""

    def __init__(self, status):
        self.__status = status

    @property
    def status(self):
        return self.__status


class Originator:
    """制作者"""

    def __init__(self):
        self.__status = None

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):  # 注意引用问题，需要的时候deepcopy
        self.__status = status

    def create_memento(self):
        memento = Memento(self.status)
        return memento


class Caretaker:
    """备忘录管理者"""

    def __init__(self):
        self.name2memento = {}

    def get_memento(self, name):
        return self.name2memento.get(name, None)

    def set_memento(self, name, memento: Memento):
        self.name2memento[name] = memento
