# 2) Make it an abstract base class by inheriting ABC class from the abc module. (To import: from abc import ABC)


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
