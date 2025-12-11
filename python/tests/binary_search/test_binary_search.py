import pytest
from python.data_structures.binary_search.binary_search  import BinarySearch


def make_bst():
    bst = BinarySearch()
    for x in [10, 5, 15, 3, 7, 12, 18]:
        bst.insert(x)
    return bst


def test_inorder():
    bst = make_bst()
    assert bst.inorder() == [3, 5, 7, 10, 12, 15, 18]


def test_contains_true():
    bst = make_bst()
    assert bst.contains(7)
    assert bst.contains(10)
    assert bst.contains(18)


def test_contains_false():
    bst = make_bst()
    assert not bst.contains(100)
    assert not bst.contains(-5)


def test_insert():
    bst = make_bst()
    bst.insert(6)
    assert bst.contains(6)
    assert bst.inorder() == [3, 5, 6, 7, 10, 12, 15, 18]


def test_delete_leaf():
    bst = make_bst()
    bst.delete(3)
    assert not bst.contains(3)
    assert bst.inorder() == [5, 7, 10, 12, 15, 18]


def test_delete_node_with_one_child():
    bst = make_bst()
    bst.delete(5)  # 5 has children 3 and 7
    assert not bst.contains(5)
    assert bst.inorder() == [3, 7, 10, 12, 15, 18]


def test_delete_node_with_two_children():
    bst = make_bst()
    bst.delete(10)  # root, two children
    assert not bst.contains(10)
    assert bst.inorder() == [3, 5, 7, 12, 15, 18]
