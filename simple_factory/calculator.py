#-*-coding:utf8-*-
class Operation(object):
    """运算类"""
    def __init__(self):
        self.number_a = 0.0
        self.number_b = 0.0

    @property
    def result(self):
        return 0.0

class OperationAdd(Operation):
    """加法运算类"""
    def __init__(self):
        super(OperationAdd, self).__init__()

    @property
    def result(self):
        return self.number_a + self.number_b

class OperationSub(Operation):
    """减法运算类"""
    def __init__(self):
        super(OperationSub, self).__init__()

    @property
    def result(self):
        return self.number_a - self.number_b

class OperationMul(Operation):
    """乘法运算类"""
    def __init__(self):
        super(OperationMul, self).__init__()

    @property
    def result(self):
        return self.number_a * self.number_b

class OperationDiv(Operation):
    """除法运算类"""
    def __init__(self):
        super(OperationDiv, self).__init__()

    @property
    def result(self):
        if self.number_b == 0:
            return u"除数不能为零"
        return self.number_a / self.number_b

class OperationFactory(object):
    """简单运算工厂"""
    @staticmethod
    def create_operation(operate):
        
        oper2operation_cls = {
            "+": OperationAdd,
            "-": OperationSub,
            "*": OperationMul,
            "/": OperationDiv,
        }
        if operate in oper2operation_cls:
            return oper2operation_cls[operate]()
        return None

def main():
    oper = OperationFactory.create_operation("+")
    oper.number_a = 1
    oper.number_b = 2
    result = oper.result
    print result

if __name__ == "__main__":
    main()
