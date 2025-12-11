class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearch:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def contains(self, key):
        return self._contains(self.root, key)

    def _contains(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        if key < node.key:
            return self._contains(node.left, key)
        return self._contains(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # no child
            if node.left is None and node.right is None:
                return None
            # one child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # two children
            succ = self._min(node.right)
            node.key = succ.key
            node.right = self._delete(node.right, succ.key)

        return node

    def _min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)


# quick test
if __name__ == "__main__":
    bst = BinarySearch()
    for x in [10, 5, 15, 3, 7]:
        bst.insert(x)

    print(bst.inorder())     # [3, 5, 7, 10, 15]
    print(bst.contains(7))   # True
    print(bst.contains(20))  # False

    bst.delete(5)
    print(bst.inorder())     # [3, 7, 10, 15]
