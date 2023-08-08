
# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.ref = None

# class Linked_List:
#     def __init__(self) -> None:
#         self.head = None

#     def print_LL(self):
#         if self.head is None:
#             print("Linked list empty")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref

#     def add_begin(self,data):
#         new_node = Node(data)
#         new_node.ref = self.head
#         self.head = new_node

# ll = Linked_List()
# ll.add_begin(10)
# ll.add_begin(30)
# ll.add_begin(50)
# ll.print_LL()


class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.ref = None

class Linked:
    def __init__(self) -> None:
        self.head = None

    def print_LL(self):
        if self is None:
            print("list empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

ll = Linked()
ll.add_begin(10)
ll.add_begin(30)
ll.add_begin(50)
ll.print_LL()

