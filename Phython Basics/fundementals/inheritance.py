#Single level
# class Parent:
#     def method1(self):
#         print("Its method1 class")
# class Child(Parent):
#     def method2(self):
#         print("its method2 ")
# c1 = Child()
# c1.method2()
# c1.method1()

# class Parent:
#     def method1(self):
#         print("Its method1 class")
# class Child(Parent):
#     pass
# c1 = Child()
# c1.method1()


#multilevel
# class Parent:
#     def method1(self):
#         print("Its method1 class")
# class Child(Parent):
#     def method2(self):
#         print("Method 2")
# class kid(Child):
#     def mehod3(self):
#         print("Kid")
# k = kid()
# k.method1()
# k.method2()
# k.mehod3()


# #multiple
# class A:
#     def method1(self):
#         print("Its method1 class")
# class B:
#     def method2(self):
#         print("Its method2 class")
# class c(A,B):
#     pass
# f = c()
# f.method1()
# f.method2()

#init
# class Parent:
#     def __init__(self):
#         print("Its parent")
# class child(Parent):
#     def __init__(self):
#         print("Child class")
#         pass
# child()

# class Parent:
#     def __init__(self):
#         print("Its parent")
# class child(Parent):
#     def __init__(self):
#         print("its child")
#         super().__init__()
# child()

# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
#     def area(self):
#      return self.length * self.breadth
# r = Rectangle(6, 3)
# print(r.area())
# class Squre(Rectangle):
#    def __init__(self, side):
#       self.side = side
#       super().__init__(side, side)
     
# sq = Squre(5)
# d =sq.area()
# print(d)

class A:
    def __init__(self) -> None:
        print("its init A")
    def feature1(self):
        print("Feature1 is working")
    def feature2(self):
        print("Feature2 is working")
class B:
    def __init__(self) -> None:
        super().__init__()
        print("its init B")
    def feature3(self):
        print("Feature3 is working")
    def feature4(self):
        print("Feature4 is working")
class C(B,A):
    def __init__(self) -> None:
        super().__init__()
        print("its init C")

C()
