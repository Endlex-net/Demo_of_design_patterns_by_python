# -*-coding:utf8-*-
class Person:
    """人(ConcreteComponent)"""

    def __init__(self, name):
        self.name = name

    def show(self):
        print u"装扮的{}".format(self.name)


class Finery():
    """服饰类(Decorator)"""

    def decorate(self, person):
        # 打扮
        self.component = person

    def show(self):
        if self.component:
            self.component.show()


class TShirts(Finery):
    """T恤(ConcreteDecorator)"""

    def show(self):
        print u"大T恤"
        Finery.show(self)


class BigTrouser(Finery):
    """垮裤(ConcreteDecorator)"""

    def show(self):
        print u"垮裤"
        Finery.show(self)


def main():
    person = Person(u"小菜")

    print "扮装"

    kk = BigTrouser()
    dtx = TShirts()

    # 修饰过程 感觉在不断的给person 增加新的职责功能
    kk.decorate(person)
    dtx.decorate(kk)
    dtx.show()


if __name__ == "__main__":
    main()
