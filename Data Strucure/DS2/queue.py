# queue = []

# def enqueue():
#     element = input("Enter the element: ")
#     queue.append(element)
#     print(queue)

# def dequeue():
#     if not queue:
#         print("queue is empty")
#     else:
#         e = queue.pop(0)
#         print("Remove ",e)

# while True:
#     print("select option 1. enqueue 2. dequeue 3. quit: ")
#     choice = int(input("Enter here: "))
#     if choice == 1:
#         enqueue()
#     elif choice == 2:
#         dequeue()
#     elif choice == 3:
#         break
#     else:
#         print("incorrect")




# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.ref = None

# class Queue:
#     def __init__(self) -> None:
#         self.head = None
#         self.tail = None

#     def empty(self):
#         return self.head is None
    
#     def enqueue(self, data):
#         new_node = Node(data)
#         if self.empty():
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.ref = new_node
#             self.tail = new_node

#     def dequeue(self):
#         if self.empty():
#             raise Exception("Queue is empty")
#         n = self.head.data
#         if self.head == self.tail:
#             self.head = None
#             self.tail = None
#         else:
#             self.head = self.head.ref
#         return n
    
#     def size(self):
#         count = 0
#         n = self.head
#         while n:
#             count += 1
#             n = n.ref
#         return count
    
#     def peek(self):
#         if self.empty():
#             raise Exception("Queue is empty")
#         return self.head.data
    
#     def display(self):
#         if self.empty():
#             print("Queue is empty")
#             return
#         n = self.head
#         while n:
#             print(n.data,"-->", end=" ")
#             n = n.ref
#         print("NULL")
    
# q = Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.enqueue(50)
# q.dequeue()
# print("size",q.size())
# print("Peek", q.peek())
# q.dequeue()
# q.display()



class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.ref = None

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def empty(self):
        return self.head is None
    
    def enqueue(self,data):
        new_node = Node(data)
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.ref = new_node
            self.tail = new_node

    def dequeue(self):
        if self.empty():
            raise Exception("Queue is empty")
        n = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.ref
        return n
    
    def display(self):
        if self.empty():
            print("Queue is empty")
        else:
            n = self.head
            while n:
                print(n.data)
                n = n.ref
            print("NULL")
    
    def even_number(self):
        even = []
        while not self.empty():
            num = self.dequeue()
            if num % 2 == 0:
                even.append(num)
        for num in reversed(even):
            print(num)

    def reverse(self):
        reversed = Queue()
        while not self.empty():
            value = self.dequeue()
            reversed.enqueue(value)
        self.head = reversed.head

        n = reversed.head
        print("reversed")
        while n:
            print(n.data,end="  ")
            n = n.ref 
        self.head = reversed.head

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(7)
q.dequeue()
# q.display()
# q.even_number()
q.reverse()