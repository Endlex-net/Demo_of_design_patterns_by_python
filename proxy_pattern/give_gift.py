# -*-coding:utf-8-*-
class IGiveGiftSubject:
    """Subject"""

    def give_dolls(self):
        pass

    def give_flowers(self):
        pass

    def give_chocolate(self):
        pass

class Proxy(IGiveGiftSubject):
    """Proxy"""
    def __init__(self, gg):
        self.gg = gg

    def give_dolls(self):
        self.gg.give_dolls()

    def give_flowers(self):
        self.gg.give_flowers()

    def give_chocolate(self):
        self.gg.give_chocolate()


class Pursuit(IGiveGiftSubject):
    """RealSubject"""
    def __init__(self, mm):
        self.mm = mm

    def give_dolls(self):
        print(u'{}送你洋娃娃'.format(self.mm.name))

    def give_flowers(self):
        print(u'{}送你花花'.format(self.mm.name))

    def give_chocolate(self):
        print(u'{}送你巧克力'.format(self.mm.name))


class SchoolGirl:
    def __init__(self, name):
        self.name = name

def main():
    mm = SchoolGirl(u"李娇娇")

    gg = Pursuit(mm)

    daili = Proxy(gg)

    daili.give_chocolate()
    daili.give_dolls()
    daili.give_flowers()


if __name__ == '__main__':
    main()

