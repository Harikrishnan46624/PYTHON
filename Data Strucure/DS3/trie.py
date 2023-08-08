class TrieNode:
    def __init__(self) -> None:
        self.child = {}
        self.end = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self,data):
        node = self.root
        for i in data:
            if i not in node.child:
                node.child[i] = TrieNode()
            node = node.child[i]
        node.end = True

    def search(self, data):
        node = self.root
        for i in data:
            if i not in node.child:
                return False
            node = node.child[i]
        return node.end
    
    def start(self, prefix):
        node = self.root
        for i in prefix:
            if i not in node.child:
                return False
            node = node.child[i]
        return True
    
    def display(self):
        words = []
        self.traverse(self.root,"",words)
        for i in words:
            print(i)

    def traverse(self, node, prefix, words):
        if node.end:
            words.append(prefix)
        for char, child in node.child.items():
            self.traverse(child, prefix + char, words)


trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("app")
trie.insert("ball")
print(trie.search("app"))
print(trie.start("na"))
# trie.display()
# print(trie.start("app"))


