class Singleton1:
    """单例模式1"""
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance


class SingletonType(type):
    """单例模式2"""
    __instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class Singleton2(metaclass=SingletonType):
    pass


def singleton_decorator(cls):
    """单例修饰器"""
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton_decorator
class Singleton3:
    pass


"""
import方法
作为python的模块是天然的单例模式
"""
from my_singleton import singleton4

if __name__ == "__main__":
    one = Singleton1()
    two = Singleton1()
    print(one is two)
    print(id(one))
    print(id(two))

    one = Singleton2()
    two = Singleton2()
    print(one is two)
    print(id(one))
    print(id(two))

    one = Singleton3()
    two = Singleton3()
    print(one is two)
    print(id(one))
    print(id(two))

    one = singleton4
    two = singleton4
    print(one is two)
    print(id(one))
    print(id(two))
