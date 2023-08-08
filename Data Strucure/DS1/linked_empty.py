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
            if n is not None:
                print(n.data)
                n = n.ref
    def add_begin(self,data):
        new_node = Node(data)
        new_node = self.head
        self.head = new_node

    
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")

ll1 = Linked_List()
ll1.add_end(60)
ll1.insert_empty(30)

ll1.print_LL()