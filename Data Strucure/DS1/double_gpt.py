class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
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

    def print_reverse(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            while current is not None:
                print(current.data, end=" ")
                current = current.prev
            print()

    def add_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
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
            new_node.prev = current

    def add_after(self, data, x):
        if self.head is None:
            print("List is empty")
        else:
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
                if current.next is not None:
                    current.next.prev = new_node
                current.next = new_node
                new_node.prev = current

    def delete(self, x):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current is not None:
                if current.data == x:
                    break
                current = current.next
            if current is None:
                print("Node not found")
            else:
                if current.prev is None:
                    self.head = current.next
                else:
                    current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                del current


# Example usage:
dll = DoublyLinkedList()
dll.add_end(10)
dll.add_end(20)
dll.add_end(30)
dll.add_end(40)
dll.add_end(50)

dll.print_list()  # Output: 10 20 30 40 50
dll.print_reverse()  # Output: 50 40 30 20 10

dll.add_after(25, 20)
dll.print_list()  # Output: 10 20 25 30 40 50

dll.delete(30)
dll.print_list()  # Output: 10 20 25 40 50
