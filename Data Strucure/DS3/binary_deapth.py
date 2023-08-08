class BST:

    def __init__(self, root) -> None:
        self.root = root
        self.left = None
        self.right = None

    def insert(self, data):
        if self.root is None:
            self.root = data
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

    def depth(self):
        if self.root is None:
            return 0
        left = self.left.depth() if self.left else 0
        right = self.right.depth() if self.right else 0
        return max(left, right) + 1
    
    def height(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return max(left_height, right_height) + 1
    
    def find_depth(self, data):
        return self._find_depth_helper(self.root, data, 0)

    def _find_depth_helper(self, node, data, depth):
        if node is None:
            return -1  # Node not found, return -1
        if node.root == data:
            return depth  # Node found, return the current depth
        if data < node.root:
            return self._find_depth_helper(node.left, data, depth + 1)
        else:
            return self._find_depth_helper(node.right, data, depth + 1)
    

b = BST(10)

b.insert(15)
b.insert(1)
b.insert(5)
b.insert(9)
b.insert(12)
b.insert(4)
# print(b.depth())  
# print(b.height())
print(b.find_depth(9))