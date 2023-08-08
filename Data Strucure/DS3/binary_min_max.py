class BST:
    def __init__(self,root) -> int:
        self.root = root
        self.left = None
        self.right = None

    def insert(self,data):
        if self.root is None:
            self.root = data
            return
        if self.root == data:
            return
        if data < self.root:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)
    
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.root,"-->",end=" ")

    def min_node(self):
        if self.left is not None:
            current = self
            while current.left:
                current = current.left
            print("smallest node: ", current.root)

    def max_node(self):
        if self.right is not None:
            current = self
            while current.right:
                current = current.right
            print("largest number: ",current.root)

b = BST(10)
list1 = [20,4,12,45,3,8]
for i in list1:
    b.insert(i)
# b.postorder() 
b.min_node()
b.max_node()