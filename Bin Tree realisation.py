
class Node:
    def __init__(self, node, key):
        self.left = None
        self.right = None
        self.node = node
        self.key = key

    def insert(self, node):
        if self.node:
            if self.node >= self.left:

                if self.left:
                    if self.left > node:
                        self.left.insert(node)
                else:
                    self.left = Node(node)
            else:
                if self.right:
                    if self.right < node:
                        self.right.insert(node)
                else:
                    self.right = Node(node)

    def search(self, node, key):
        if self.node is None or key == self.node.key:
            return node
        if key < self.node.key:
            return self.left.search(self.left, key)
        else:
            return self.right.search(self.right, key)

    def max(self, node):
        if self.right:
            return self.right
        else:
            return node

    def min(self, node):
        if self.left:
            return self.left
        else:
            return node
