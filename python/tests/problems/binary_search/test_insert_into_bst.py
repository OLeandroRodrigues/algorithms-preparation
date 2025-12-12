from problems.binary_search.insert_into_bst import BinarySearchTree


def test_insert_into_empty_tree():
    bst = BinarySearchTree()
    bst.insert(10)

    assert bst.root is not None
    assert bst.root.key == 10


def test_insert_left_child():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)

    assert bst.root.left is not None
    assert bst.root.left.key == 5


def test_insert_right_child():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(15)

    assert bst.root.right is not None
    assert bst.root.right.key == 15


def test_insert_multiple_elements():
    bst = BinarySearchTree()
    values = [10, 5, 15, 3, 7, 12, 18]

    for v in values:
        bst.insert(v)

    # inorder traversal should be sorted
    assert inorder(bst.root) == [3, 5, 7, 10, 12, 15, 18]


def test_insert_duplicate_is_ignored():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(10)

    assert bst.root.key == 10
    assert bst.root.left is None
    assert bst.root.right is None


# ---------- helper ----------
def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.key] + inorder(node.right)
