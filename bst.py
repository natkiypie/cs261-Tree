

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
