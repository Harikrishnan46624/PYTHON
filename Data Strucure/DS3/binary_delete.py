class BST:
    def __init__(self, root) -> None:
        self.root = root
        self.left = None
        self.right = None

    def insert(self, data):
        if self.root is None:
            self.root = data
            return
        if self.root == data:
            return
        if self.root > data:
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
                print("Given number is not present")
        elif data > self.root:
            if self.right:
                self.right = self.right.delete(data, curr)
            else:
                print("Given number is not present")
        else:
            if self.left is None:
                temp = self.right
                if data == curr:
                    self.root = temp.root
                    self.left = temp.left
                    self.right = temp.right
                    temp = None
                    return self
                self = None
                return temp
            node = self.right
            while node.left:
                node = node.left
            self.root = node.root
            self.right = self.right.delete(node.root, curr)
        return self
   
    def preorder(self):
        print(self.root,"-->",end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

   
root = BST(10)
list1 = [6,3,4,5,7,89,12]
for i in list1:
    root.insert(i)            
root.delete(7)
root.preorder()

