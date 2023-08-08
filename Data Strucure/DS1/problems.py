# # Write a Python program to create a singly linked list, append some items and iterate through the list.
# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.ref = None

# class Linked:
#     def __init__(self) -> None:
#         self.head = None
#         self.end = None
#         self.count = 0
#     def iterate_item(self):
#         n = self.head
#         while n:
#             val = n.data
#             n = n.ref
#             yield val
#     def append(self,data):
#         new_node = Node(data)
#         if self.end:
#             self.end.ref = new_node
#             self.end = new_node
#         else:
#             self.head = new_node
#             self.end = new_node
#         self.count += 1

# ll = Linked()
# ll.append("PHP")
# ll.append("Python")
# ll.append("SQL")
# ll.append("C#")
# ll.append("C++")
# ll.append("Django")
# for val in ll.iterate_item():
#     print(val)
# print("\nhead.data: ",ll.head.data)
# print("end.data: ",ll.end.data)


# Write a Python program to find the size of a singly linked list
# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.ref = None

# class Linked:
#     def __init__(self) -> None:
#         self.head = None
#         self.end = None
#         self.count = 0

#     def iterate_item(self):
#         n = self.head
#         while n:
#             val = n.data
#             n = n.ref
#             yield val

#     def append(self,data):
#         new_node = Node(data)
#         if self.end:
#             self.end.ref = new_node
#             self.end = new_node
#         else:
#             self.head = new_node
#             self.end = new_node
#         self.count += 1

# ll = Linked()
# ll.append("PHP")
# ll.append("Python")
# ll.append("SQL")
# ll.append("C#")
# ll.append("C++")
# ll.append("Django")
# ll.iterate_item()
# for val in ll.iterate_item():
#     print(val)
# print("size of the list: ",ll.count)


# . Write a Python program to search a specific item in a singly linked list and return true if the item is found otherwise return false.
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.ref = None

class Linked:
    def __init__(self) -> None:
        self.head = None
        self.end = None
        self.count = 0

    def append(self,data):
        new_node = Node(data)
        if self.head:
            self.head.ref = new_node
            self.head = new_node
        else:
            self.end = new_node
            self.head = new_node
        self.count += 1

    def iterate_item(self):
        n = self.end
        while n:
            val = n.data
            n = n.ref
            yield val

    def search(self,val):
        for new_node in self.iterate_item():
            if val == new_node:
                return True
        return False
        
ll = Linked()
ll.append("PHP")
ll.append("Python")
ll.append("SQL")
ll.append("C#")
ll.append("C++")
ll.append("Django")

for val in ll.iterate_item():
    print(val)

if ll.search("C#"):
    print("\nTrue")
else:
    print("\nFalse")