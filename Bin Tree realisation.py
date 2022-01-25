from random import randint


class Node:
    def __init__(self, node, key):
        self.left = None
        self.right = None
        self.node = node
        self.key = key

    def insert(self, node):
        if self.node:
            if node <= self.node:
                if self.left is None:
                    self.left = Node(node, node)
                else:
                    self.left.insert(node)
            if node > self.node:
                if self.right is None:
                    self.right = Node(node, node)
                else:
                    self.right.insert(node)

    def search(self, key):
        if self.node is None or key == self.key:
            return self.node
        if key < self.key:
            return self.left.search(key)
        else:
            return self.right.search(key)

    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self.node

    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self.node


def mintest():
    x = randint(1, 1000)
    node = Node(x, x)
    ansm = node.node
    for i in range(100000):
        a = randint(1, 1000)
        node.insert(a)
        ansm = min(ansm, a)
        if ansm == node.min():
            continue
        else:
            print("error, min=", ansm, 'wrong answer=', node.min())


def maxtest():
    x = randint(1, 1000)
    node = Node(x, x)
    ansmx = node.node
    for i in range(100000):
        a = randint(1, 1000)
        node.insert(a)
        ansmx = max(ansmx, a)
        if ansmx == node.max():
            continue
        else:
            print("error, min=", ansmx, 'wrong answer=', node.max())


def searchtest():
    check = []
    x = randint(1, 1000)
    node = Node(x, x)
    for i in range(1000):
        a = randint(1, 1000)
        node.insert(a)
        check.append(a)
    for j in range(len(check)):
        if node.search(check[j]) is not None:
            continue
        else:
            print('error')

mintest()
maxtest()
searchtest()
