class Register:
    """报到登记"""

    def register(self, name: str):
        print(F"活动中心{name}报道成功！")


class Payment:
    """缴费中心"""

    def pay(self, name, money):
        print(f"缴费中心：收到{name}同学{money}元付款，缴费成功！")


class Dormitory:
    """宿舍"""

    def meet_roommate(self, name):
        print(f"宿舍: 大家好！这是刚来的{name}同学, 是你们未来需要共度四年的舍友！互相认识一下!")


class Volunteer:
    """志愿者"""

    def __init__(self, name):
        self.name = name
        self.register = Register()
        self.payment = Payment()
        self.life_center = Dormitory()

    def welcome_freshmen(self, name):
        print(f"{name}同学，你好! 我是志愿者{self.name}, 我将带你完成整个报道流程")

        self.register.register(name)
        self.payment.pay(name, 1000)
        self.life_center.meet_roommate(name)


if __name__ == "__main__":
    volunteer = Volunteer("Clay")
    volunteer.welcome_freshmen("Endlex")
