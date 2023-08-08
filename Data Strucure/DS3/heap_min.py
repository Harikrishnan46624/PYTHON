class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def parent(self, i):
        return (i -1) // 2
    
    def left(self, i):
        return 2 * i + 1
    
    def right(self,i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap)- 1)

    def delete(self):
        if not self.heap:
            return None
        self.swap(0, len(self.heap) - 1)
        min_value = self.heap.pop()
        self.heapify_down(0)
        return min_value
    
    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
                self.swap(i, self.parent(i))

    def heapify_down(self, i):
        left = self.left(i)
        right = self.right(i)
        smallest = i

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.swap(i, smallest)
            self.heapify_down(smallest)

    def display(self):
        print(self.heap)

h = MinHeap()
list1 = [50,12,11,72,15,20]
for i in list1:
    h.insert(i)
# min_value = h.extract_min()
# print(min_value)
h.display()