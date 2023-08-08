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

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.nref is None:
            self.head = None
            print("DL is empty")

        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    def delete_value(self,x):
        if self.head is None:
            print("List is empty")
            return
        if self.head.nref is None:
            if x == self.head.data:
                self.head = None
            else:
                print("x not present")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print("x not present")
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node


ll = Double_LL()
ll.add_begin(10)
ll.add_begin(30)
ll.add_begin(50)
ll.delete_value(30)
ll.print_LL()
