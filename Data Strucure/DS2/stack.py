# stack = []

# def push():
#     elemnt = input("Enter the element: ")
#     stack.append(elemnt)
#     print(stack)

# def pop_element():
#     if not stack:
#         print("Stack  is empty")
#     else:
#         e = stack.pop()
#         print("removed element: ",e)
#         print(stack)

# while True:
#     print("select option 1. push 2. pop 3. quit: ")
#     choice = int(input())
#     if choice == 1:
#         push()
#     elif choice == 2:
#         pop_element()
#     elif choice == 3:
#         break
#     else:
#         print("incorrect")


class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.ref = None

class Stack:
    def __init__(self) -> None:
        self.top = None

    def empty(self):
        return self.top is None
    
    def push(self,data):
        new_node = Node(data)
        new_node.ref = self.top
        self.top = new_node

    def pop(self):
        if self.empty():
            return None
        pop_node = self.top
        self.top = self.top.ref
        pop_node.ref = None
        return pop_node.data
    
    def peek(self):
        if self.empty():
            return None
        return self.top.data
    
    def display(self):
        if self.empty():
            print("stack is empty")
            return
        n = self.top
        while n:
            print(n.data,"-->", end=" ")
            n = n.ref
        print("NULL")

    def reverse(self):
        reversed_stack = Stack()
        while not self.empty():
            value = self.pop()
            reversed_stack.push(value)
        self.top = reversed_stack.top

        n = reversed_stack.top
        print("reversed")
        while n:
            print(n.data,"-->",end=" ")
            n = n.ref
        print("NULL")
        self.top = reversed_stack.top

    def even_numbers(self):
        even = []
        while not self.empty():
            num = self.pop()
            if num % 2 == 0:
                even.append(num)
                
        for num in reversed(even):
            print(num)
        
    def size(self):
        count = 0
        n = self.top
        while n:
            count += 1
            n = n.ref
        return count
        


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(15)
# print(s.pop())
# print(s.peek())
# print(s.empty())
# s.display()
s.reverse()
# s.even_numbers()


