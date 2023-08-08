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
                print(n.data,"--->",end=" ")
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
                print(n.data,"--->",end=" ")
                n = n.pref

    def add_after(self,data,x):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("given node not present LL")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not Node:
                    n.nref.pref = new_node
                n.nref = new_node

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

    def add_before(self,data,x):

        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("given node not present LL")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref= new_node
                else:
                    self.head = new_node
                n.pref = new_node


dl = Double_LL()
dl.add_end(10)
dl.add_end(20)
dl.add_end(30)
dl.add_end(40)
dl.add_end(50)
dl.add_after(90,20)
dl.print_LL()
dl.print_L_reverse()    
      