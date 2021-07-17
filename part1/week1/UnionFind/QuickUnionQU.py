# Quick Union (Lazy approach)
# Created by: Mohammed Mounir, Bouhamed
# Date: July 17, 2021

class QuickUnionQU:

    def __init__(self, n):
        self.id = list(range(n))

    def root(self, i):
        while self.id[i] != i:
            i = self.id[i]

        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        p_root = self.root(p)
        q_root = self.root(q)
        self.id[p_root] = self.id[q_root]


test = QuickUnionQU(10)
test.union(4, 3)
test.union(3, 8)
test.union(6, 5)
test.union(9, 4)
test.union(2, 1)

print(test.connected(8, 9))
print(test.connected(5, 4))

test.union(5, 0)
test.union(7, 2)
test.union(6, 1)
test.union(7, 3)

print(test.id)
