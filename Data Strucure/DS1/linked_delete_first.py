class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.ref = None

class Linked_List:
    def __init__(self) -> None:
        self.head = None

    def print_LL(self):
        if self.head is None:
            print('list empty')
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def delet_first(self):
        if self.head is None:
            print('Node is empty')
        else:
            self.head = self.head.ref



ll = Linked_List()
ll.add_end(30)
ll.add_end(60)
ll.add_end(90)
ll.add_end(120)
ll.delet_first()
ll.print_LL()