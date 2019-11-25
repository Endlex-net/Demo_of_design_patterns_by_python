class DataClass:
    def __init__(self, value1, value2, value3):
        self._value1 = value1
        self._value2 = value2
        self._value3 = value3

    @property
    def value1(self):
        return self._value1

    @property
    def value2(self):
        return self._value2

    @property
    def value3(self):
        return self._value3


class MainClass:
    def __init__(self, value1, value2, value3):
        self.data = DataClass(value1, value2, value3)

    def sum(self):
        return sum([self.data.value1, self.data.value2, self.data.value3])


def main():
    m = MainClass(1, 3, 5)
    print(m.sum())


if __name__ == "__main__":
    main()
