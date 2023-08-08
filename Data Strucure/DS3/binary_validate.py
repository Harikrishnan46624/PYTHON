class BST:
    def __init__(self, root) -> None:
        self.root =  root
        self.left = None
        self.right = None

    def insert(self, data):
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

    def delete(self, data, curr = None):
        if self.root is None:
            print("Tree is empty")
            return
        if data < self.root:
            if self.left:
                self.left = self.left.delete(data, curr)
            else:
                print("Not found in tree")
        elif data > self.root:
            if self.right:
                self.right = self.right.delete(data, curr)
            else:
                print("NOt present in Tree")
        else:
            if self.left is None:
                temp = self.right
                if data == curr:
                    self.root = temp.root
                    self.left = temp.left
                    self.right = temp.right
                    temp = None
                    return self
                node = self.right
                while node.left:
                    node = node.left
                self.root = self.right.delete(node.root, curr)
        return self
    
    def search(self,data):
        if self.root == data:
            print("Node is found")
        if data < self.root:
            if self.left:
                self.left.search(data)
            else:
                print("Node is not present")
        else:
            if self.right:
                self.right.search(data)
            else:
                print("Node is not found")

   
    def min_value(self):
        if self.left is not None:
            return self.left.min_value()
        return self.root

    def max_value(self):
        if self.right is not None:
            return self.right.max_value()
        return self.root

    def preorder(self):
        print(self.root,"-->",end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def validate_bst(self):
        if self is  None:
            return True
        if (self.left is not None and self.left.max_value() > self.root):
            return False
        if (self.right is not None and self.right.min_value() < self.root):
            return False
        if (self.left is not None and self.left.validate_bst()):
            return False
        if (self.right is not None and self.right.validate_bst()):
            return False
        return True
    
    def preorder(self):
        print(self.root,"-->", end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    

root = BST(10)
list1 = [6,3,4,5,7,89,12]
for i in list1:
    root.insert(i) 

# print(root.max_value())
# print(root.min_value())
# print(root.validate_bst())

root.preorder()