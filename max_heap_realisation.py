from random import randint
import sys
class MaxHeap:

    def __init__(self, maxsize):

        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        return pos // 2

    def lchild(self, pos):
        return 2 * pos

    def rchild(self, pos):

        return (2 * pos) + 1

    def isChild(self, pos):

        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):

        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],
                                            self.Heap[fpos])

    def maxrootdel(self, pos):

        if not self.isChild(pos):
            if (self.Heap[pos] < self.Heap[self.lchild(pos)] or
                    self.Heap[pos] < self.Heap[self.rchild(pos)]):

                if (self.Heap[self.lchild(pos)] >
                        self.Heap[self.rchild(pos)]):
                    self.swap(pos, self.lchild(pos))
                    self.maxrootdel(self.lchild(pos))

                else:
                    self.swap(pos, self.rchild(pos))
                    self.maxrootdel(self.rchild(pos))

    def insert(self, elem):

        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = elem

        cnum = self.size

        while (self.Heap[cnum] >
               self.Heap[self.parent(cnum)]):
            self.swap(cnum, self.parent(cnum))
            cnum = self.parent(cnum)


    def extractMax(self):

        mas = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxrootdel(self.FRONT)

        return mas

for i in range (100):
    mas = []
    maxHeap = MaxHeap(1000)
    for k in range(100):
        x = randint(1, 1000)
        maxHeap.insert(x)
        mas.append(x)
    ans = max(mas)
    if ans == maxHeap.extractMax():
        continue
    else:
        print(ans, maxHeap.extractMax())
