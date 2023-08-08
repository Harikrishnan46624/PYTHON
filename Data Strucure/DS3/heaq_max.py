# # import heapq

# # heap = []
# # heapq.heappush(heap,10)
# # heapq.heappush(heap,1)
# # heapq.heappush(heap,5)
# # heapq.heappush(heap,0)
# # heapq.heappush(heap,3)
# # heapq.heappush(heap,6)
# # print(heap)

# # list1 = [1,3,5,2,4,6]
# # heapq.heapify(list1)
# # heapq.heappushpop(list1,89)
# # heapq.heapreplace(list1,100)
# # print(list1)

# # list1 = [1,3,5,2,4,6]
# # heapq.nsmallest(2,list1)
# # print(list1)


# class MaxHeap:
#     def __init__(self):
#         self.heap = []
    
#     def parent(self, i):
#         return (i - 1) // 2
    
#     def left_child(self, i):
#         return 2 * i + 1
    
#     def right_child(self, i):
#         return 2 * i + 2
    
#     def swap(self, i, j):
#         self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
#     def insert(self, item):
#         self.heap.append(item)
#         self.heapify_up(len(self.heap) - 1)
    
#     def extract_max(self):
#         if not self.heap:
#             return None
#         self.swap(0, len(self.heap) - 1)
#         max_value = self.heap.pop()
#         self.heapify_down(0)
#         return max_value
    
#     def heapify_up(self, i):
#         while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
#             self.swap(i, self.parent(i))
#             i = self.parent(i)
    
#     def heapify_down(self, i):
#         n = len(self.heap)
#         left = self.left_child(i)
#         right = self.right_child(i)
#         largest = i
        
#         if left < n and self.heap[left] > self.heap[largest]:
#             largest = left
        
#         if right < n and self.heap[right] > self.heap[largest]:
#             largest = right
        
#         if largest != i:
#             self.swap(i, largest)
#             self.heapify_down(largest)
    
#     def print_heap(self):
#         print(self.heap)


# # Create a MaxHeap instance
# heap = MaxHeap()

# # Insert elements into the heap
# heap.insert(5)
# heap.insert(10)
# heap.insert(3)
# heap.insert(8)
# heap.insert(2)

# # Print the Max Heap
# heap.print_heap()

# # Extract the maximum element
# max_value = heap.extract_max()
# print(max_value)  # Output: 10


class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2
    
    def left(self, i):
        return 2 * i + 1
    
    def right(self, i):
        return 2 * i + 2
    
    def swap(self, i ,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        self.swap(0 , len(self.heap) - 1)
        max_value = self.heap.pop()
        self.heapify_down(0)
        return max_value
    
    def heapify_up(self,i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify_down(self, i):
        n = len(self.heap)
        left = self.left(i)
        right = self.right(i)
        largest = i

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.swap(i, largest)
            self.heapify_down(largest)

    def display(self):
        print(self.heap)

heap = MaxHeap()
heap.insert(5)
heap.insert(10)
heap.insert(3)
heap.insert(8)
heap.insert(2)
heap.insert(90)
heap.display()
print(heap.extract_max())


