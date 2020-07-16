from abc import ABC, abstractmethod

# write a class that extends a special class ABC
class Calculator(ABC):
    @abstractmethod
    def add(self, num1, num):
        pass


class CasioCalculator(Calculator):
    def add(self, num1, num):
        print(num1 + num)


calc = CasioCalculator()
calc.add(1, 2)
