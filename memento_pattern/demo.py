from abc import ABC, abstractmethod


class Memento:
    """备忘录"""

    def __init__(self, status):
        self.__status = status

    @property
    def status(self):
        return self.__status


class Originator:
    """制作者"""

    def __init__(self):
        self.__status = None

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):  # 注意引用问题，需要的时候deepcopy
        self.__status = status

    def create_memento(self):
        memento = Memento(self.status)
        return memento

    def set_memento(self, memento):
        self.status = memento.status


class Caretaker:
    """备忘录管理者"""

    def __init__(self):
        self.name2memento = {}

    def get_memento(self, name):
        return self.name2memento.get(name, None)

    def add_memento(self, name, memento: Memento):
        self.name2memento[name] = memento


class Game(Originator):
    """游戏内容"""

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.status = 0
        print(f"{self.name}已经运行了!")

    def next_step(self):
        self.status = self.status + 1
        print(f"{self.name}游戏运行到了第{self.status}阶段")

    def set_load(self, load):
        self.set_memento(load)
        print(f"游戏加载至{self.status}阶段")


class GameLoadManager(Caretaker):
    """游戏存档管理"""

    def __init__(self, game):
        self.game = game
        super().__init__()

    def show_loads(self):
        print(f"已经保存如下存档：")
        for name in self.name2memento.keys():
            print(f"\t-{name}")

    def save_load(self, name):
        load = self.game.create_memento()
        self.add_memento(name, load)
        print("存档保存成功")

    def checkout_load(self, name):
        """加载存档存档"""
        load = self.get_memento(name)
        if load:
            print(f"{name}已经加载至游戏{self.game.name}")
            self.game.set_load(load)
        else:
            print("无效存档")


if __name__ == "__main__":
    game = Game("超级玛丽")
    game.next_step()
    game_load_manager = GameLoadManager(game)
    game_load_manager.save_load('游戏存档1')
    game.next_step()
    game.next_step()
    game_load_manager.save_load("游戏存档2")
    game_load_manager.show_loads()
    game_load_manager.checkout_load("游戏存档1")
