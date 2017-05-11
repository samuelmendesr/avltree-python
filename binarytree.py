from node import Node

class BinaryTree:

    def __init__(self):
        self._root = None

    def insert(self, data):
        if self._root:
            self._insert(self._root, data)
        else:
            self._root = Node(data)

    def remove(self, data):
        node = self._find(self._root, data)
        if node:
            self._remove(node)

    def preorder(self):
        self._preorder(self._root)

    def inorder(self):
        self._inorder(self._root)

    def postorder(self):
        self._postorder(self._root)

    def _insert(self, node, data):
        if data > node.data:
            if node.right:
                self._insert(node.right, data)
            else:
                node.setRight(Node(data))
        elif data < node.data:
            if node.left:
                self._insert(node.left, data)
            else:
                node.setLeft(Node(data))

    def _find(self, node, data):
        if node:
            if node.data == data:
                return node
            elif node.data < data:
                return self._find(node.right, data)
            elif node.data > data:
                return self._find(node.left, data)
        else:
            return None

    def _findMin(self, node):
        if node.left:
            return self._findMin(node.left)
        else:
            return node

    def _findMax(self, node):
        if node.right:
            return self._findMax(node.right)
        else:
            return node

    def _remove(self, node):
        if node.left and node.right:
            min = self._findMin(node.right)
            node.data = min.data
            min.parent.setRight(min.right)
        elif node.left:
            if node.parent:
                if node.parent.right:
                    node.parent.setRight(node.left)
                else:
                    node.parent.setLeft(node.left)
            else:
                self._root = node.left
                self._root.parent = None
        elif node.right:
            if node.parent:
                if node.parent.right:
                    node.parent.setRight(node.right)
                else:
                    node.parent.setLeft(node.right)
            else:
                self._root = node.right
                self._root.parent = None
        else:
            if node.parent:
                if node.parent.right:
                    node.parent.setRight(None)
                else:
                    node.parent.setLeft(None)
            else:
                self._root = None

    def _preorder(self, node):
        if node:
            print(node)
            self._preorder(node.left)
            self._preorder(node.right)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node)
            self._inorder(node.right)

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node)
