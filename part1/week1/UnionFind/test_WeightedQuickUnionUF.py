from unittest import TestCase

from part1.week1.UnionFind.WeightedQuickUnionUF import WeightedQuickUnionUF


class TestQuickUnionUF(TestCase):

    def test_connected(self):
        wqf = WeightedQuickUnionUF(10)
        wqf.union(4, 3)
        wqf.union(3, 8)
        wqf.union(5, 6)
        wqf.union(9, 4)
        wqf.union(1, 2)
        self.assertTrue(wqf.connected(8,9))

    def test_not_connected(self):
        wqf = WeightedQuickUnionUF(10)
        wqf.union(4, 3)
        wqf.union(3, 8)
        wqf.union(5, 6)
        wqf.union(9, 4)
        wqf.union(1, 2)
        self.assertFalse(wqf.connected(5,0))

    def test_connected(self):
        wqf = WeightedQuickUnionUF(10)
        wqf.union(4, 3)
        wqf.union(3, 8)
        wqf.union(5, 6)
        wqf.union(9, 4)
        wqf.union(1, 2)
        wqf.union(5, 0)
        wqf.union(7,2)
        wqf.union(6,1)
        self.assertTrue(wqf.connected(5, 0))