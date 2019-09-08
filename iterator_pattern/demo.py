from typing import List, Optional


class BaseIterator:
    """迭代器"""

    def __init__(self, data):
        self.__data = data
        self.__cur_index = 0

    def to_begin(self):
        """将指针移动至初始位置"""
        self.__cur_index = 0

    def next(self):
        try:
            ret = self.__data[self.__cur_index + 1]
            self.__cur_index += 1
        except IndexError:
            ret = None
        return ret

    def has_next(self):
        return self.__cur_index >= len(self.__data)

    def current(self):
        return self.__data[self.__cur_index]


class Customer:
    """客户"""

    def __init__(self, name):
        self.__name = name
        self.__num = None
        self.__clinic = None

    @property
    def name(self):
        return self.__name

    def register(self, system):
        system.push_customer(self)

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def clinic(self):
        return self.__clinic

    @clinic.setter
    def clinic(self, clinic):
        self.__clinic = clinic


class NumeralIterator(BaseIterator):
    """迭代器"""

    def __init__(self, customers: List[Customer]):
        super().__init__(customers)


class NumeralSystem:
    """排号系统"""
    __clinics = ("1诊室", "2诊室", "3诊室",)

    def __init__(self, name):
        self.__customers: List[Customer] = []
        self.__cur_num = 0
        self.__name = name

    def push_customer(self, customer: Customer):
        cur_num = self.__cur_num + 1
        customer.num = cur_num
        click = NumeralSystem.__clinics[cur_num % len(NumeralSystem.__clinics) - 1]
        customer.clinic = click
        self.__customers.append(customer)
        self.__cur_num = cur_num

    def get_iterator(self):
        return NumeralIterator(self.__customers)


if __name__ == "__main__":
    numeral_system = NumeralSystem("挂号台")
    endlex = Customer("Endlex")
    endlex.register(numeral_system)
    clay = Customer("Clay")
    clay.register(numeral_system)
    alex = Customer("Alex")
    alex.register(numeral_system)
    tony = Customer("Tony")
    tony.register(numeral_system)
    print()

    iterator = numeral_system.get_iterator()
    while iterator.next():
        customer = iterator.current()
        print(f"下一位病人: {customer.name} 请到{customer.clinic}")
