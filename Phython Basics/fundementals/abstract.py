from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("its running")

com1 = Laptop()
com1.process()

from abc import ABC,abstractmethod
class Vehicle(ABC):
    def color(self):
        print("White")
    @abstractmethod
    def gear(self):
        pass

class Car(Vehicle):
    def gear(self):
        print("Its automatic")
        
a = Car()
a.gear()