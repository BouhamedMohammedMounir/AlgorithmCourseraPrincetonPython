# Description: Quick union algorithm (Lazy approach) implemented in Python
# Python version: 3.8
# Created by: BMM
# Date: 2020 oct 31

class QuickUnionUF:

    def __init__(self, N):
        self.id = list(range(N))

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]

        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j