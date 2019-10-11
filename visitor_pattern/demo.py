from abc import ABC, abstractmethod


class DataNode(ABC):
    """数据结构类"""

    def accept(self, visitor):
        """接受访问者的访问"""
        visitor.visit(self)


class Visitor(ABC):
    """访问者"""

    @abstractmethod
    def visit(self, data):
        """对数据进行访问"""
        pass


class ObjectStructure:
    """数据结构的管理类， 也是数据对象的一个容器，可遍历容器内的所有元素"""

    def __init__(self):
        self.__datas = []

    def add(self, data_element):
        self.__datas.append(data_element)

    def action(self, visitor):
        """进行数据访问的操作"""
        for data in self.__datas:
            data.accept(visitor)


class Animal(DataNode):
    """动物类"""

    def __init__(self, name, is_male, age, weight):
        self.__name = name
        self.__is_male = is_male
        self.__age = age
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @property
    def is_male(self):
        return self.__is_male

    @property
    def age(self):
        return self.__age

    @property
    def weight(self):
        return self.__weight


class Cat(Animal):
    """🐱喵"""

    def speak(self):
        print("Miao!!~~")


class Dog(Animal):
    """狗"""

    def speak(self):
        print("wang！！！～")


class GenderCounter(Visitor):
    """性别统计"""

    def __init__(self):
        self.male_cat = 0
        self.female_cat = 0
        self.male_dog = 0
        self.female_dog = 0

    def visit(self, data):
        if isinstance(data, Cat):
            if data.is_male:
                self.male_cat += 1
            else:
                self.female_cat += 1

        elif isinstance(data, Dog):
            if data.is_male:
                self.male_dog += 1
            else:
                self.female_dog += 1

    def get_info(self):
        print(f"{self.male_cat}只公猫, {self.female_cat}只母猫, {self.male_dog}只公狗, {self.female_dog}只母狗")


class WeightCounter(Visitor):
    """体重统计"""

    def __init__(self):
        self.cat_num = 0
        self.cat_weight = 0
        self.dog_num = 0
        self.dog_weight = 0

    def visit(self, data):
        if isinstance(data, Cat):
            self.cat_num += 1
            self.cat_weight += data.weight
        elif isinstance(data, Dog):
            self.dog_num += 1
            self.dog_weight += data.weight

    def get_info(self):
        print(f"猫的平均重量是{self.cat_weight / self.cat_num} , 狗的平均重量是{self.dog_weight / self.dog_num}")


if __name__ == "__main__":
    animals = ObjectStructure()
    animals.add(Cat("cat1", True, 1, 5))
    animals.add(Cat("cat2", True, 0.7, 4))
    animals.add(Cat("cat3", True, 1.7, 5))
    animals.add(Dog("dog1", True, 1.3, 9))
    animals.add(Dog("dog2", True, 3, 55))
    animals.add(Dog("dog3", True, 1, 21))

    gender_counter = GenderCounter()
    animals.action(gender_counter)
    gender_counter.get_info()

    weight_counter = WeightCounter()
    animals.action(weight_counter)
    weight_counter.get_info()
