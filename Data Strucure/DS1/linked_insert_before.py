class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
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

    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty")
            
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found")
        

ll1 = LinkedList()
ll1.add_end(10)
ll1.add_end(20)
ll1.add_end(30)
ll1.add_end(40)
ll1.add_end(50)
ll1.add_before(5,30)
ll1.add_before(5,60)
ll1.print_LL()