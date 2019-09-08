from abc import ABC, abstractmethod


class Component(ABC):
    """组件"""

    @abstractmethod
    def display(self):
        pass


class Composite(Component):
    """组合"""

    def __init__(self):
        self.__components = []

    def add(self, component: Component):
        self.__components.append(component)

    def remove(self, component):
        self.__components.remove(component)

    def display(self):
        for component in self.__components:
            component.display()


class CPU(Component):
    """cpu"""

    def __init__(self, name):
        super().__init__()
        self.name = name

    def display(self):
        print(f"cpu: {self.name}, 可以进行高速运算.")


class MemoryCard(Component):
    """内存条"""

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"内存: {self.name}, 内存可以高速存储软件运行需要的数据")


class HardDisk(Component):
    """硬盘"""

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"硬盘: {self.name}, 可以存储数据，不容易丢失")


class Computer(Composite):
    """电脑"""

    def __init__(self, name):
        self.name = name
        super().__init__()

    def display(self):
        print(f"电脑：{self.name}, 由以下组件组成")
        super().display()


if __name__ == "__main__":
    computer = Computer("Endlex's Computer")
    computer.add(CPU('Intel i7'))
    computer.add(MemoryCard("16G 高速内存条"))
    computer.add(HardDisk("512G SSD"))
    computer.display()
