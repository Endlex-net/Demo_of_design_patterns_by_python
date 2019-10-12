from abc import ABC, abstractmethod
from typing import List


class Element:
    def __init__(self, name):
        self.name = name


class Filter(ABC):

    @abstractmethod
    def do_filter(self, elements: List[Element]) -> List[Element]:
        pass


class FilterChain:
    """过滤器链"""

    def __init__(self):
        self.__filters: List[Filter] = []

    def add_filter(self, filter: Filter) -> None:
        """增加过滤器"""
        assert isinstance(filter, Filter), TypeError()
        self.__filters.append(filter)

    def do_filter(self, elements: List[Element]) -> List[Element]:
        for filter in self.__filters:
            elements = filter.do_filter(elements)
        return elements


class SiltFilter(Filter):
    """泥沙过滤"""

    def do_filter(self, elements: List[Element]) -> List[Element]:
        for element in elements:
            if element.name == "泥沙":
                elements.remove(element)
        return elements


class IncrustationFilter(Filter):
    """水垢过滤"""

    def do_filter(self, elements: List[Element]) -> List[Element]:
        for element in elements:
            if element.name == "水垢":
                elements.remove(element)
        return elements


if __name__ == "__main__":
    water_purifier = FilterChain()
    water_purifier.add_filter(SiltFilter())
    water_purifier.add_filter(IncrustationFilter())

    elements = [Element("泥沙"), Element("水垢"), Element("水"), Element("水"), Element("水垢"),]
    elements = water_purifier.do_filter(elements)
    for element in elements:
        print(element.name)
