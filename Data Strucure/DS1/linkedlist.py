# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.ref = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def print_LL(self):
#         if self.head is None:
#             print("Linked List empty")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref
# LL1 = LinkedList()
# LL1.head = Node(10)
# LL1= Node(20)
# LL1.print_LL()


# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.nref = None
#         self.pref = None

# class Doubly_Linked_List:
#     def __init__(self) -> None:
#         self.head = None

#     def print_LL(self):
#         if self.head is None:
#             print('list is empty')
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.nref
#     def print_LL_reverse(self):
#         if self.head is None:
#             print('list is empty')
#         else:
#             n = self.head
#             while n.nref is not None:
                
#                 n = n.pref
#             while n is not None:
#                  print(n.data)
#                  n = n.pref

