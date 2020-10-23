# Description: Quick find algorithm (Eager approach) implemented in Python
# Python version: 3.8
# Created by: BMM
# Date: 2020 oct 23

class QuickFindUF:

    def __init__(self, N):
        self.ID = [i for i in range(N)]

    def connected(self, p, q):
        return self.ID[p] == self.ID[q]

    def union(self, p, q):
        pID = self.ID[p]
        qID = self.ID[q]
        for i, iID in enumerate(self.ID):
            if iID == pID:
                self.ID[i] = qID

qf = QuickFindUF(10)

qf.union(4, 3)
qf.union(3, 8)
qf.union(5, 6)
qf.union(9, 4)
qf.union(1, 2)

print(qf.connected(8,9))
print(qf.connected(5,0))

qf.union(5,0)
qf.union(7,2)
qf.union(6,1)

print(qf.connected(5,0))