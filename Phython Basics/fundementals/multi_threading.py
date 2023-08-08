# import threading
# print(threading.current_thread().getName())


# def func1():
#     for i in range(1,51):
#         print(i)
# def func2():
#     for i in range(100, 200):
#         print(i)
# func1()
# func2()


from threading import Thread
from time import sleep
class A(Thread):
    def run(self):
        for i in range(1,10):
            print(i)
            sleep(1)
class B(Thread):
    def run(self):
        for j in range(10, 20):
            print(j)
            sleep(1)
a1 = A()
b1 =B()
a1.start()
sleep(0.2)
b1.start()
a1.join()
b1.join()
print("complete")
      