
import unittest

from bst import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A BinarySearchTree exists.
        """
        try:
            BinarySearchTree()
        except NameError:
            self.fail("Could not instantiate BinarySearchTree")

    def test_instantiation_with_value(self):
        fake_value = "fake"
        bst = BinarySearchTree(fake_value)
        self.assertEqual(fake_value, bst.value)

    def test_has_left_and_right_initially_none(self):
        bst = BinarySearchTree()
        self.assertEqual(None, bst.left)
        self.assertEqual(None, bst.right)

    def test_insert_smaller_values_as_left(self):
        bst = BinarySearchTree(10)
        child = BinarySearchTree(5)
        bst.insert(child)
        self.assertEqual(child, bst.left)

    def test_insert_larger_values_as_right(self):
        bst = BinarySearchTree(5)
        child = BinarySearchTree(10)
        bst.insert(child)
        self.assertEqual(child, bst.right)

if __name__ == '__main__':
    unittest.main()
