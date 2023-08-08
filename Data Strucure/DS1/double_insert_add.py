class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.nref = None
        self.pref = None

class Double_LL:
    def __init__(self) -> None:
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("LIst is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.nref

    def print_L_reverse(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.nref
            while n is not None:
                print(n.data,"--.",end=" ")
                n = n.pref

    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("LL is not empty")

    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n .nref = new_node
            new_node.pref = n

dl = Double_LL()
dl.insert_empty(10)     
dl.add_begin(20)
dl.add_end(100)
dl.print_LL()
dl.print_L_reverse()    