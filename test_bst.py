
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

    def test_find(self):
        test_val = 10
        bst = BinarySearchTree(test_val)
        return_val = bst.find(test_val)
        self.assertEqual(test_val, return_val)

    def test_find_for_none(self):
        val = None
        bst = BinarySearchTree()
        test_val = bst.find(10)
        self.assertEqual(test_val, val)

    def test_find_smaller_value(self):
        val = 10
        sml_val = 5
        bst = BinarySearchTree()
        bst.insert(val)
        bst.insert(sml_val)
        test_val = bst.find(sml_val)
        self.assertEqual(test_val, sml_val)

    def test_find_larger_value(self):
        val = 10
        lrg_val = 15
        bst = BinarySearchTree()
        bst.insert(val)
        bst.insert(lrg_val)
        test_val = bst.find(lrg_val)
        self.assertEqual(test_val, lrg_val)

    def test_find_multiple_values(self):
        val_one = 10
        val_two = 5
        val_three = 2
        bst = BinarySearchTree()
        bst.insert(val_one)
        bst.insert(val_two)
        bst.insert(val_three)
        test_val = bst.find(val_three)
        self.assertEqual(test_val, val_three)

    def test_preorder(self):
        bst = BinarySearchTree()
        bst.insert(3)
        bst.insert(1)
        bst.insert(7)
        bst.insert(5)
        test_list = [3, 1, 7, 5]
        test_case = bst.preorder()
        self.assertEqual(test_case, test_list)

    def test_inorder(self):
        bst = BinarySearchTree()
        bst.insert(3)
        bst.insert(1)
        bst.insert(7)
        bst.insert(5)
        test_list = [1, 3, 5, 7]
        test_case = bst.inorder()
        self.assertEqual(test_case, test_list)

    def test_postorder(self):
        bst = BinarySearchTree()
        bst.insert(3)
        bst.insert(1)
        bst.insert(7)
        bst.insert(5)
        test_list = [1, 5, 7, 3]
        test_case = bst.postorder()
        self.assertEqual(test_case, test_list)

if __name__ == '__main__':
    unittest.main()
