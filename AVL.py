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
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

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

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def insert(self, key, value, node=None):
        if node is None:
            node = self.root

        if not node:
            return Node(key, value)

        if key < node.key:
            node.left = self.insert(key, value, node.left)
        elif key > node.key:
            node.right = self.insert(key, value, node.right)
        else:
            node.value = value
            return node

        node.height = self._new_height(node)
        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)

        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)

        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def add(self, key, value):
        self.root = self.insert(key, value, self.root)

    def remove(self, key, node=None):
        if node is None:
            node = self.root

        if not node:
            return None

        if key < node.key:
            node.left = self.remove(key, node.left)
        elif key > node.key:
            node.right = self.remove(key, node.right)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self.remove(temp.key, node.right)

        node.height = self._new_height(node)
        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)

        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)

        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def delete(self, key):
        self.root = self.remove(key, self.root)

    def inOrderTraversal(self, node=None):
        if node is None:
            node = self.root
        if not node:
            return
        self.inOrderTraversal(node.left)
        print(node.key, node.value)
        self.inOrderTraversal(node.right)
