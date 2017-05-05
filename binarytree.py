from node import Node

class BinaryTree:
    def __init__(self):
        self._root = None;
    def insert(self, data):
        if self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
    def _insert(self, node, data):
        if data > node.data:
            if node.right == 0:
                node.right = Node(data)
            else:
                self._insert(node.right, data)
        elif data < node.data:
            if node.left == 0:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
    def remove(self, data):
        #...
    #def preorder(self):
    #def inorder(self):
    #def postorder(self):
    #def remove(self, data):
    #def search(self, data):
