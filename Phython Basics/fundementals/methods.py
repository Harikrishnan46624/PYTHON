# class Car:

#     @staticmethod
#     def add (a, b):
#         return a+ b
# a = Car.add(10, 12)
# print(a)



# class Book:
#     def read(self):
#         print('Started reading books')
# Book1 = Book()
# Book1.read()


#instance method
# class Car:
#     def __init__(self,color,make,model,gps=False):
#         self.color = color
#         self.make = make
#         self.model = model
#         self.gps = gps
#     def car_info(self): #get method/getter
#         print(f'Make : {self.make}\ncolor : {self.color}\nmodel : {self.model}')
#     def set_gps(self):  #set method/setter
#         self.gps = True
#         print('GPS enabled')
# car1 = Car('Red', 'BMW', 2020)
# car1.car_info()
# car1.set_gps
# car1.gps


#Class mthods
# class car:
#     wheels = 4
#     @classmethod
#     def get_wheels_count(cls):
#         return cls.wheels
# b = car.get_wheels_count()
# print(b)

class Student:
    school = "FLYNN"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3
    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        print("this is something")
a1 = Student(10,20,30)
a2 = Student(40,50,60)
print(a1.avg())
print(Student.getschool())
Student.info()


# class Student:
#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#     def avg(self):
#         return(self.m1 + self.m2 + self.m3)/3
#     def getm1(self):
#         return self.m1
#     def setm1(self,value):
#         self.m1 = value
# a1 = Student(10,20,30)
# a2 = Student(40,50,60)
# a1.setm1(90)
# print(a1.avg())
# print(a2.avg())

# 