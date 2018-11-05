

class BinarySearchTree:

    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, node):
        if self.value == None:
            self.value = node
        elif node < self.value:
            self.left = node
        else: 
            self.right = node

