from abc import ABC
from typing import List
from functools import cmp_to_key


class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def show(self):
        print(f"{self.name} 年龄:{self.age} 体重:{self.weight} 身高:{self.height}")


class ICompare(ABC):
    """比较算法抽象类"""

    def comparable(self, person1: Person, person2: Person) -> bool:
        pass


class CompareByAge(ICompare):
    def comparable(self, person1: Person, person2: Person) -> bool:
        return person1.age - person2.age


class CompareByHeight(ICompare):
    def comparable(self, person1: Person, person2: Person) -> bool:
        return person1.height - person2.height


class CompareByWeight(ICompare):
    def comparable(self, person1: Person, person2: Person) -> bool:
        return person1.weight - person2.weight


def person_sort(persons: List[Person], compare: ICompare) -> None:
    person_count = len(persons)
    persons.sort(key=cmp_to_key(compare.comparable))
    for person in persons:
        person.show()
    print()


if __name__ == "__main__":
    persons = [
        Person("Endlex", 2, 54, 0.82),
        Person("Clay", 32, 66, 1.8),
        Person("Pencil", 54, 44, 1.7)
    ]
    person_sort(persons, CompareByAge())
    person_sort(persons, CompareByHeight())
    person_sort(persons, CompareByWeight())
