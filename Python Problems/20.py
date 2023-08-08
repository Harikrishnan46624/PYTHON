from abc import ABC, abstractmethod
class Calculator(ABC):
    @abstractmethod
    def add(self, x, y):
        pass
    @abstractmethod
    def sub(self, x, y):
        pass
    @abstractmethod
    def mul(self, x, y):
        pass
    @abstractmethod
    def div(self, x, y):
        pass

class BasicClaculator(Calculator):
    def add(self, x, y):
        return x + y
    def sub(self, x, y):
       return x - y
    def mul(self, x, y):
        return x * y
    def div(self, x, y):
       if y == 0:
           return "Cannot Divide by zero"
       return x / y
    
Calculator = BasicClaculator()

print("1 + 2 =", Calculator.add(1, 2))
print("4 - 2 =", Calculator.sub(4, 2))
print("3 * 5 =", Calculator.mul(3, 5))
print("6 / 3 =", Calculator.div(6, 3))
print("10 / 1 =", Calculator.div(10, 1))
