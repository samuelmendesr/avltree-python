class Node:
    def __init__(self, data, right = None, left = None, parent = None):
        self.data = data
        self.right = right
        self.left = left
        self.parent = parent
    def __str__(self):
        return str(self.data)
    def setRight(self, node):
        self.right = node
        if node:
            node.parent = self
    def setLeft(self, node):
        self.left = node
        if node:
            node.parent = self
