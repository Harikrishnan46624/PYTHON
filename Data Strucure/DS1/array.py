# def calc(list1,n):
#     for i in range(0,len(list1)):
#         for j in range(i+1,len(list1)):
#             if list1[i] + list1[j] == n:
#                 list1[i]
#                 return list1[i], list1[j]
#     return False
            
# print(calc([10,4,30,6,9],10))


# def calc(list1,n):
#     seen = set()
#     for num in  list1:
#         complement = n - num
#         if complement in seen:
#             return True
#         seen.add(num)
#     return False

# list1 = [10,4,30,6,9]       
# n = 10
# c = calc(list1,n)
# # print(c)

# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.ref = None

# class Linked_List:
#     def __init__(self) -> None:
#         self.head = None
#     def print_LL(self):
#         if self.head is None:
#             print("List is empty")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref
#     def add_begin(self,data):
#         new_node = Node(data)
#         new_node.ref = self.head
#         self.head = new_node

# ll = Linked_List()
# ll.add_begin(10)
# ll.add_begin(30)
# ll.add_begin(40)
# ll.print_LL()


# Python3 implementation of the approach

# Structure of a Node
# class node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None

# # Function to add a new node
# # to the Linked List
# def add(data):

# 	newnode = node(0)
# 	newnode.data = data
# 	newnode.next = None
# 	return newnode

# # Function to print the array contents
# def printArr(a, n):

# 	i = 0
# 	while(i < n):
# 		print (a[i], end = " ")
# 		i = i + 1

# # Function to return the length
# # of the Linked List
# def findlength( head):

# 	curr = head
# 	cnt = 0
# 	while (curr != None):
	
# 		cnt = cnt + 1
# 		curr = curr.next
	
# 	return cnt

# # Function to convert the
# # Linked List to an array
# def convertArr(head):

# 	# Find the length of the
# 	# given linked list
# 	len1 = findlength(head)

# 	# Create an array of the
# 	# required length
# 	arr = []

# 	index = 0
# 	curr = head

# 	# Traverse the Linked List and add the
# 	# elements to the array one by one
# 	while (curr != None):
# 		arr.append( curr.data)
# 		curr = curr.next
	
# 	# Print the created array
# 	printArr(arr, len1)

# # Driver code
# head = node(0)
# head = add(1)
# head.next = add(2)
# head.next.next = add(3)
# head.next.next.next = add(4)
# head.next.next.next.next = add(5)
# convertArr(head)

# This code is contributed by Arnab kundu


# Roy T14:50
# [https://www.simplilearn.com/tutorials/data-structure-tutorial](https://www.simplilearn.com/tutorials/data-structure-tutorial)

# [https://www.coursera.org/learn/trees-graphs-basics](https://www.coursera.org/learn/trees-graphs-basics)  (in depth)

# [https://www.youtube.com/watch?v=8hly31xKli0](https://www.youtube.com/watch?v=8hly31xKli0)      freecodecamp

# [https://www.youtube.com/watch?v=RBSGKlAvoiM](https://www.youtube.com/watch?v=RBSGKlAvoiM)   freecodecamp 

# [https://www.youtube.com/watch?v=B31
# Grind75



# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.ref = None


# def convert(arr):
#         if not arr:
#              return None
#         head = Node(arr[0])
#         n = head

#         for i in range(1,len(arr)):
#             new_node = Node(arr[i])
#             n.ref = new_node 
#             n = new_node
#         return head
# def print_ll(head):
#      if head is None:
#           print("List is empty")
#      n = head
#      while n:
#           print(n.data)
#           n= n.ref

# arr = [1,2,3,4,10]
# ll = convert(arr)
# print_ll(ll)


