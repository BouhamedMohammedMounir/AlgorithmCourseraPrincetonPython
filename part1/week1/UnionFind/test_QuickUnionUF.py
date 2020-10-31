from unittest import TestCase

from part1.week1.UnionFind.QuickUnionUF import QuickUnionUF


class TestQuickUnionUF(TestCase):

    def test_connected(self):
        qu = QuickUnionUF(10)
        qu.union(4, 3)
        qu.union(3, 8)
        qu.union(5, 6)
        qu.union(9, 4)
        qu.union(1, 2)
        self.assertTrue(qu.connected(8, 9))

    def test_not_connected(self):
        qu = QuickUnionUF(10)
        qu.union(4, 3)
        qu.union(3, 8)
        qu.union(5, 6)
        qu.union(9, 4)
        qu.union(1, 2)
        self.assertFalse(qu.connected(5,0))

    def test_connected(self):
        qu = QuickUnionUF(10)
        qu.union(4, 3)
        qu.union(3, 8)
        qu.union(5, 6)
        qu.union(9, 4)
        qu.union(1, 2)
        qu.union(5, 0)
        qu.union(7,2)
        qu.union(6,1)
        self.assertTrue(qu.connected(5, 0))