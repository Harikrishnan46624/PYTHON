#          
# print(dir(str))
# class Car:
#     def __init__(self,color,price,km):
#         self.color = color
#         self.price = price
#         self.km = km
#     def __len__ (self):
#         return self.km
#     def __add__(self,other):
#         return self.price + other.price
    
# car1 = Car('red', 50000,5000)
# car2 = Car('blue', 40000,10000)
# print(len(car1))
# x = car1 + car2
# print(x)

#Duck Typing
class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")
class MyEditors:
    def execute(self):
        print("spell check")
        print("Convention")
class Laptop:
    def code(self,ide):
        ide.execute()
        
ide = MyEditors()

lap1 = Laptop()
