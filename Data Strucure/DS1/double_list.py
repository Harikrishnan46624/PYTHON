class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.nref = None
        self.pref = None

class dobly_LL:
    def __init__(self) -> None:
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.nref

    def print_LL_reverse(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
            while n is not None:
                print(n.data)
                n = n.pref

dl = dobly_LL()
dl.print_LL()
dl.print_LL_reverse()