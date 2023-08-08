class BST:
    def __init__(self,root) -> None:
        self.root = root
        self.left = None
        self.right = None

    def insert(self,data):
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

    def search(self,data):
        if self.root == data:
            print("Node is found")
            return
        if self.root > data:
            if self.left:
                self.left.search(data)
            else:
                print("NOde is not present")
        else:
            if self.right:
                self.right.search(data)
            else:
                print("NOde is not present")

    def preorder(self):
        print(self.root,"-->", end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.root,"-->",end=" ")
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.root,"-->",end=" ")
        

b = BST(10)
list1 = [20,4,12,45,3,8]
for i in list1:
    b.insert(i)
print("PRE-ORDER")
b.preorder()
print("\nIN-ORDER")
b.inorder() 
print("\nPOST-ORDER")
b.postorder()