# -*-coding:utf8-*-
import abc


class CashSuper:
    """收费父类"""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def accept_cash(self, money):
        pass


class CashNormal(CashSuper):
    """正常收费"""

    def accept_cash(self, money):
        return money


class CashRebate(CashSuper):
    """折扣收费"""

    def __init__(self, money_rebate=1.0):
        self.money_rebate = money_rebate

    def accept_cash(self, money):
        return self.money_rebate * money


class CashReturn(CashSuper):
    """满返收费"""

    def __init__(self, money_condition, money_return):
        self.money_condition = money_condition
        self.money_return = money_return

    def accept_cash(self, money):
        if money >= self.money_condition:
            return money - self.money_return
        return money


class CashContext(object):
    """收费上下文"""

    def __init__(self, cash_name):
        self.csuper = None
        cash_name2cash_obj = {
            u"正常收费": CashNormal,
            u"打八折": lambda: CashRebate(0.8),
            u"满300返100": lambda: CashReturn(300, 100),
        }
        if cash_name in cash_name2cash_obj:
            self.csuper = cash_name2cash_obj[cash_name]()

    def get_result(self, money):
        return self.csuper.accept_cash(money)


def main():
    display = ""
    total = 0.0
    cbx_txt = u"打八折"
    amount = 2
    price = 20.0
    csuper = CashContext(cbx_txt)
    total_prices = csuper.get_result(price * amount)
    total += total_prices
    display += u"单价：{}\t数量: {}\t {}\t合计: {}".format(price, amount, cbx_txt, total_prices)
    print display
    print u"总计：{}".format(total)


if __name__ == "__main__":
    main()
