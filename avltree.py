'''
AVLTree Python

autor: Samuel Mendes Rodrigues
last update: 11/05/2017

'''
from binarytree import BinaryTree

class AVLTree(BinaryTree):

    def insert(self, data):
        super().insert(data)
        self._root = self.__balance(self._root)

    def remove(self, data):
        super().remove(data)
        self._root = self.__balance(self._root)

    def __rightRotate(self, x):
        y = x.right
        x.setRight(y.left)
        y.setLeft(x)
        return y

    def __leftRotate(self, x):
        y = x.left
        x.setLeft(y.right)
        y.setRight(x)
        return y

    def __rightLeftRotate(self, x):
        x.setRight(self.__leftRotate(x.right))
        return self.rightRotate(x)

    def __leftRightRotate(self, x):
        x.setLeft(self.__rightRotate(x.left))
        return self.leftRotate(x)

    def __balance(self, node):
        if node.left:
            node.setLeft(self.__balance(node.left))
        if node.right:
            node.setRight(self.__balance(node.right))

        y = None
        if node.balance() < -1 or node.balance() > 1:
            if node.balance() < -1:
                if node.left.balance() < 0:
                    y = self.__leftRotate(node)
                else:
                    y = self.__leftRightRotate(node)

            if node.balance() > 1:
                if node.right.balance() > 0:
                    y = self.__rightRotate(node)
                else:
                    y = self.__rightLeftRotate(node)

            if node == self._root:
                y.parent = None

            node = y

        return node
