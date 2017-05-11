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
    def high(self):
        lh = self.left.high() if self.left else -1
        rh = self.right.high() if self.right else -1
        return rh + 1 if rh > lh else lh + 1
    def balance(self):
        lh = self.left.high() if self.left else 0
        rh = self.right.high() if self.right else 0
        return rh - lh
