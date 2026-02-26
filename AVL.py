class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.height = 1
        self.left = None
        self.right = None


class AVL_Phone_Book:

    def __init__(self):
        self.root = None

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _new_height(self, node):
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = self._new_height(y)
        x.height = self._new_height(x)
        return x

    def _left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = self._new_height(x)
        y.height = self._new_height(y)
        return y

    def insert(self, key, value, node=None):
        if node is None:
            if self.root is None:
                self.root = Node(key, value)
                return self.root
            node = self.root

        if key < node.key:
            node.left = self.insert(key, value, node.left)
        elif key > node.key:
            node.right = self.insert(key, value, node.right)
        else:
            node.value = value
            return node

        node.height = self._new_height(node)
        balance = self._get_balance(node)

        # Left Left
        if balance > 1 and key < node.left.key:
            if node == self.root:
                self.root = self._right_rotate(node)
                return self.root
            return self._right_rotate(node)

        # Left Right
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            if node == self.root:
                self.root = self._right_rotate(node)
                return self.root
            return self._right_rotate(node)

        # Right Right
        if balance < -1 and key > node.right.key:
            if node == self.root:
                self.root = self._left_rotate(node)
                return self.root
            return self._left_rotate(node)

        # Right Left
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            if node == self.root:
                self.root = self._left_rotate(node)
                return self.root
            return self._left_rotate(node)

        if node == self.root:
            self.root = node

        return node

    def remove(self, node, key):
        # if not node:
        #     return node

        # if key < node.key:
        #     node.left = self.remove(node.left, key)
        pass

    def get(self, key):
        pass

    def contains(self, key):
        pass

    def inOrderTraversal(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return

        self.inOrderTraversal(node.left)
        print(node.key, node.value)
        self.inOrderTraversal(node.right)
