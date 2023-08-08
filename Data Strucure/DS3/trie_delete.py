class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, data):
        node = self.root
        for char in data:
            if char not in node.child:
                node.child[char] = TrieNode()
            node = node.child[char]
        node.end = True

    def delete_help(self, node):
        for char, child in node.child.items():
            self.delete_help(child)
            node.child = {}
            node.end = False

    def delete_all(self):
        self.delete_help(self.root)

    def display(self):
        words = []
        self.traverse(self.root, "", words)
        for word in words:
            print(word)

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
# trie.delete_all()
# trie.display()

