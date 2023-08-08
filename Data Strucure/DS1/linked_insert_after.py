class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.ref = None
        
class Linked_List:
    def __init__(self) -> None:
        self.head = None

    def Print_LL(self):
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
            
    def add_after(self,data,x):
        n = self.head 
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


ll1 = Linked_List()
ll1.add_begin(10)
ll1.add_begin(30)
ll1.add_after(50,30)
ll1.Print_LL()