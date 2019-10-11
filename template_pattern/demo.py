from abc import ABC, abstractmethod


class Template(ABC):
    """模版类(抽象类)"""

    @abstractmethod
    def step_one(self):
        pass

    @abstractmethod
    def step_two(self):
        pass

    def template_methold(self):
        print("第一步，准备：")
        self.step_one()
        print("第二步，准备：")
        self.step_two()


class TemplateImplA(Template):
    """模版实现类A"""

    def step_one(self):
        print("A的第一步")

    def step_two(self):
        print("A的第二步")


class TemplateImplB(Template):
    """模版实现类B"""

    def step_one(self):
        print("B的第一步")

    def step_two(self):
        print("B的第一步")


if __name__ == "__main__":
    a = TemplateImplA()
    a.template_methold()
    b = TemplateImplB()
    b.template_methold()
