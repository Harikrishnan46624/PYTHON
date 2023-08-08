class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print()

    def add_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def add_after(self, data, x):
        current = self.head
        while current is not None:
            if current.data == x:
                break
            current = current.next
        if current is None:
            print("Node not found")
        else:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node

    def delete(self, x):
        if self.head is None:
            print("List is empty")
        elif self.head.data == x:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None:
                if current.next.data == x:
                    current.next = current.next.next
                    break
                current = current.next
            else:
                print("Node not found")


# Example usage:
ll = LinkedList()
ll.add_end(10)
ll.add_end(20)
ll.add_end(30)
ll.add_end(40)
ll.add_end(50)

ll.print_list()  # Output: 10 20 30 40 50

ll.add_front(5)
ll.add_front(1)

