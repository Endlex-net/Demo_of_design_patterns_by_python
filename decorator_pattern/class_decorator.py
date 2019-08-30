class ClassDecorator:
    """修饰类"""

    def __init__(self, func):
        # 在第一次修饰的时候被初始化
        self.__count = 0
        self.__func = func

    def __call__(self, *args, **kwargs):
        self.__count += 1
        obj = self.__func(*args, **kwargs)
        print(f"{self.__func.__name__}: {self.__count}")
        return obj


@ClassDecorator
class A:
    pass


@ClassDecorator
class B:
    pass


if __name__ == "__main__":
    a = A()
    a2 = A()
    b = B()
