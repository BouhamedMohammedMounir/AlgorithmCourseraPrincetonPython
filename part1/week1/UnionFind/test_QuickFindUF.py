from unittest import TestCase

from part1.week1.UnionFind.QuickFindUF import QuickFindUF


class TestQuickFindUF(TestCase):
    def test_connected(self):
        qf = QuickFindUF(10)
        qf.union(4, 3)
        qf.union(3, 8)
        qf.union(5, 6)
        qf.union(9, 4)
        qf.union(1, 2)
        self.assertTrue(qf.connected(8,9))

    def test_not_connected(self):
        qf = QuickFindUF(10)
        qf.union(4, 3)
        qf.union(3, 8)
        qf.union(5, 6)
        qf.union(9, 4)
        qf.union(1, 2)
        self.assertFalse(qf.connected(5,0))

    def test_connected(self):
        qf = QuickFindUF(10)
        qf.union(4, 3)
        qf.union(3, 8)
        qf.union(5, 6)
        qf.union(9, 4)
        qf.union(1, 2)
        qf.union(5, 0)
        qf.union(7,2)
        qf.union(6,1)
        self.assertTrue(qf.connected(5, 0))
