class Person:
    """人(ConcreteComponent)"""

    def __init__(self, name):
        self.name = name

    def show(self):
        print("装扮的{}".format(self.name))


class Finery(Person):
    """服饰类(Decorator)"""

    def __init__(self, component):
        # 继承了被装饰类 貌似更好一点
        self.__component = component

    def show(self):
        assert NotImplementedError


class TShirts(Finery):
    """T恤(ConcreteDecorator)"""

    def show(self):
        print("大T恤")
        super().show()


class BigTrouser(Finery):
    """垮裤(ConcreteDecorator)"""

    def show(self):
        print(u"垮裤")
        super().show()


def main():
    person = Person(u"小菜")

    print("扮装")

    # 修饰过程 感觉在不断的给person 增加新的职责功能
    kk = TShirts(person)
    kk = BigTrouser(kk)
    kk.show()
    print(isinstance(kk, Person))


if __name__ == "__main__":
    main()
