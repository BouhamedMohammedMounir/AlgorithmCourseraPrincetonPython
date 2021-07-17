# Optimized Quick Union (Lazy approach)
# Created by: Mohammed Mounir, Bouhamed
# Date: July 17, 2021

class WeightedQuickUnionWQU:

    def __init__(self, n):
        self.id = list(range(n))
        self.size = [1] * n

    def root(self, i):
        while self.id[i] != i:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]

        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        p_root = self.root(p)
        q_root = self.root(q)
        if p_root == q_root:
            return

        if self.size[p_root] < self.size[q_root]:
            self.id[p_root] = self.id[q_root]
            self.size[q_root] += self.size[p_root]
        else:
            self.id[q_root] = self.id[p_root]
            self.size[p_root] += self.size[q_root]


with open('tinyUF.txt') as f:
    N = int(next(f))
    test = WeightedQuickUnionWQU(N)
    array = []
    for line in f:  # read rest of lines
        if line != '':
            p, q =[int(x) for x in line.split()]
            test.union(p, q)


print(test.id)
