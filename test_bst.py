
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

#    def test_insert_smaller_values_as_left(self):
#        bst = BinarySearchTree(10)
#        child = BinarySearchTree(5)
#        bst.insert(child)
#        self.assertEqual(child, bst.left)
#
#    def test_insert_larger_values_as_right(self):
#        bst = BinarySearchTree(5)
#        child = BinarySearchTree(10)
#        bst.insert(child)
#        self.assertEqual(child, bst.right)

    def test_new_insert_method(self):
        value = 10
        bst = BinarySearchTree()
        bst.insert(value)
        self.assertEqual(value, bst.value)

    def test_insert_value_left(self):
        value = 10
        new_value = 5
        bst = BinarySearchTree()
        bst.insert(value)
        bst.insert(new_value)
        self.assertEqual(new_value, bst.left.value)

    def test_insert_value_right(self):
        value = 10
        new_value = 15
        bst = BinarySearchTree()
        bst.insert(value)
        bst.insert(new_value)
        self.assertEqual(new_value, bst.right.value)

    def test_multiple_insertions(self):
        val_one = 1
        val_two = 5
        val_three = 10
        val_four = 15
        bst = BinarySearchTree()
        bst.insert(val_three)
        bst.insert(val_two)
        bst.insert(val_four)
        bst.insert(val_one)
        self.assertEqual(val_one, bst.left.left.value)



if __name__ == '__main__':
    unittest.main()
