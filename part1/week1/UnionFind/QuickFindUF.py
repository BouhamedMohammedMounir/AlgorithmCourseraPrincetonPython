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
