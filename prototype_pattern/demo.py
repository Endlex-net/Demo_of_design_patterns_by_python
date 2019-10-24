import copy
from abc import ABC


class Prototype(ABC):
    def clone(self):
        return copy.deepcopy(self)


class Realizetype(Prototype):
    def show(self):
        return id(self)


if __name__ == "__main__":
    obj = Realizetype()
    obj2 = obj.clone()
    print(obj.show(), obj2.show())
