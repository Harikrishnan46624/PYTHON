class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.ref = None

class Linked_List:
    def __init__(self) -> None:
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def delete_value(self,x):
        if self.head is None:
            print("List is empty")
        if self.head.data == x:
            self.head = self.head.ref
        else:
            n = self.head
            while n is not None:
                if n.ref.data == x:
                    n.ref = n.ref.ref
                    break
                n = n.ref

                
ll = Linked_List()
ll.add_begin(10)
ll.add_begin(20)
ll.add_begin(30)
ll.delete_value(20)
ll.print_LL()