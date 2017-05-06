from node import Node

class BinaryTree:
    def __init__(self):
        self._root = None

    def insert(self, data):
        if self._root:
            self._insert(self._root, data)
        else:
            self._root = Node(data)

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

    def remove(self, data):#melhorar depois
        node = self._find(self._root, data)

        if node:
            self._remove(node)

    def _remove(self, node):#melhorar depois
        if node.left and node.right:
            min = self._findMin(node.right)
            node.data = min.data
            min.parent.setLeft(min.right)
        else:
            parent = {'setChild':None}

            if node.parent:
                if node.parent.right == node:
                    parent['setChild'] = node.parent.setRight
                else:
                    parent['setChild'] = node.parent.setLeft

            if node.left:
                if node.parent:
                    parent['setChild'](node.left)
                else:
                    _root = node.left
                    _root.parent = None
            elif node.right:
                if node.parent:
                    parent['setChild'](node.right)
                else:
                    _root = node.right
                    _root.parent = None
            else:
                if node.parent:
                    parent['setChild'](None)
                else:
                    _root = None
    #def preorder(self):
    #def inorder(self):
    #def postorder(self):
