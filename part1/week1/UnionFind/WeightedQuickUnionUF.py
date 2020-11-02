# Description: Quick union algorithm (Lazy approach) implemented in Python
# Python version: 3.8
# Created by: BMM
# Date: 2020 oct 31

class WeightedQuickUnionUF:

    def __init__(self, N):
        self.id = list(range(N))
        self.size = list(1 for i in range(N))

    def find(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]

        return i

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return

        if self.size[i] < self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]