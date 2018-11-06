

class BinarySearchTree:

    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, node):
        if self.value is None:
            self.value = node
        elif node < self.value:
            if self.left is None:
                self.left = BinarySearchTree(node)
            else:
                self.left.insert(node)
        elif node > self.value:
            if self.right is None:
                self.right = BinarySearchTree(node)
            else:
                self.right.insert(node)

    def find(self, value):
        if self.value is None:
            return None
        elif self.value is value:
            return self.value
        elif value < self.value:
            return self.left.find(value)
        elif value > self.value:
            return self.right.find(value)

    def preorder(self):
        po_list = [self.value]
        if self.left:
            po_list.extend(self.left.preorder())
        if self.right:
            po_list.extend(self.right.preorder())
        return po_list

