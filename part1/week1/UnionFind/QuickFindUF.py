# Quick Find (Eager approach)
# Created by: Mohammed Mounir, Bouhamed
# Date: July 10, 2021

class QuickFindUF:

    def __init__(self, n):
        self.id = list(range(0, n))

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        p_id = self.id[p]
        q_id = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == p_id:
                self.id[i] = q_id


with open('tinyUF.txt') as f:
    N = int(next(f))
    test = QuickFindUF(N)
    array = []
    for line in f:  # read rest of lines
        if line != '':
            p, q =[int(x) for x in line.split()]
            test.union(p, q)


print(test.id)
