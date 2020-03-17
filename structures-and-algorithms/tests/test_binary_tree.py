from ..components.binary_tree import BinaryTree
import unittest


class TestBinaryTree(unittest.TestCase):

    def testAdd(self):
        binary_tree = BinaryTree()
        binary_tree.add(2)
        binary_tree.add(0)
        binary_tree.add(4)
        binary_tree.add(3)
        binary_tree.add(5)
        self.assertEqual(binary_tree.to_list(), [0, 2, 3, 4, 5])

    def testSearch(self):
        binary_tree = BinaryTree()
        binary_tree.add(2)
        binary_tree.add(0)
        binary_tree.add(4)
        binary_tree.add(6)
        self.assertEqual(binary_tree.search(1), 2)


if __name__ == '__main__':
    unittest.main()
