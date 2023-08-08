class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.nref = None
        self.pref = None

class Linked:
    def __init__(self) -> None:
        self.head = None
        self.end = None
        self.count = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.end = self.head
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node
        self.count += 1

    def iter(self):
        n = self.head
        while n:
            val = n.data
            n = n.nref
            yield val

    def print_forward(self):
        for node in self.iter():
            print(node)

    def search(self,x):
        for node in self.iter():
            if x == node:
                return True
        return False
    
    def delete(self,data):
        n = self.head
        node_delete = False
        if n is None:
            node_delete = False
        elif n.data == data:
            self.head = n.nref
            self.head.pref = None
            node_delete = True
        elif self.end.data == data:
            self.end = self.end.pref
            self.end.nref = None
            node_delete = True
        else:
            while n:
                if n.data == data:
                    n.pref.nref = n.nref
                    n.nref.pref = n.pref
                    node_delete = True
                n = n.nref
        if node_delete:
                self.count -= 1
ll = Linked()
ll.append("PHP")
ll.append("Python")
ll.append("SQL")
ll.append("C#")
ll.append("C++")
ll.append("Django")

print("Original list: ")
ll.print_forward()

ll.delete("C#")
ll.delete("Django")
print("After deleting")
ll.print_forward()