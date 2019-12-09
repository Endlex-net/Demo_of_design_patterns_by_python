from typing import List
from abc import ABC, abstractmethod


class IExpression(ABC):

    @abstractmethod
    def interpret(self, info: str) -> bool:
        pass


class TerminalExpression(IExpression):
    def interpret(self, info: str) -> bool:
        raise NotImplementedError


class NoTerminalExpression(IExpression):
    def interpret(self, info: str) -> bool:
        raise NotImplementedError


class MemberExpression(TerminalExpression):
    """会员"""

    def __init__(self, names: List[str]):
        self.__names = names

    def interpret(self, name: str) -> bool:
        return name in self.__names


class FootExpression(TerminalExpression):
    """食物"""

    def __init__(self, foots: List[str]):
        self.__foots = foots

    def interpret(self, foot: str) -> bool:
        return foot in self.__foots


class MemberEatFootExpression(NoTerminalExpression):
    def __init__(self, member_expression: MemberExpression, foot_expression: FootExpression):
        self.member_expression = member_expression
        self.foot_expression = foot_expression

    def interpret(self, info: str) -> (bool, str):
        strs = info.split("想吃")
        if len(strs) != 2:
            errmsg = "语法错误"
            return False, errmsg

        if not self.member_expression.interpret(strs[0]):
            errmsg = f"{strs[0]}不是我们的会员"
            return False, errmsg

        if not self.foot_expression.interpret(strs[1]):
            errmsg = f"我们没有{strs[1]}这款菜"
            return False, errmsg

        errmsg = f"{strs[0]}请稍等，即将为您提供{strs[1]}"
        return True, errmsg


class Context:
    def __init__(self):
        member_expression = MemberExpression(["小明", "小马", "老王"])
        foot_expression = FootExpression(["蛋炒饭", "粉蒸牛肉", "鱼香肉丝"])
        self.member_eat_foot_expression = MemberEatFootExpression(member_expression, foot_expression)

    def opertion(self, info: str):
        success, errmsg = self.member_eat_foot_expression.interpret(info)
        print(errmsg)
        if success:
            print("大厨登场\n")
        else:
            print("暂时无法为您服务\n")


def main():
    context = Context()
    context.opertion("小明想吃粉蒸牛肉")
    context.opertion("小马想吃宫保鸡丁")
    context.opertion("老史想吃鱼香肉丝")


if __name__ == "__main__":
    main()
