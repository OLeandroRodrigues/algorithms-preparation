import pytest
from data_structures.linkedlist.circular_linked_list.circular_linked_list import CircularLinkedList


def test_new_list_is_empty():
    cll = CircularLinkedList()
    assert cll.is_empty()
    assert len(cll) == 0
    assert repr(cll) == "CircularLinkedList([])"


def test_add_first_single_element():
    cll = CircularLinkedList()
    cll.add_first(10)

    assert not cll.is_empty()
    assert len(cll) == 1
    assert cll.get_first() == 10
    assert cll.get_last() == 10

    # circular property: tail.next is head and head is tail
    assert cll.tail is not None
    assert cll.tail.next is cll.tail


def test_add_first_multiple_elements():
    cll = CircularLinkedList()
    cll.add_first(10)
    cll.add_first(20)
    cll.add_first(30)

    # list is [30, 20, 10]
    assert len(cll) == 3
    assert cll.get_first() == 30
    assert cll.get_last() == 10

    repr_str = repr(cll)
    assert repr_str == "CircularLinkedList([30, 20, 10])"


def test_add_last_single_and_multiple():
    cll = CircularLinkedList()

    cll.add_last(10)
    assert len(cll) == 1
    assert cll.get_first() == 10
    assert cll.get_last() == 10

    cll.add_last(20)
    cll.add_last(30)

    # list is [10, 20, 30]
    assert len(cll) == 3
    assert cll.get_first() == 10
    assert cll.get_last() == 30
    assert repr(cll) == "CircularLinkedList([10, 20, 30])"


def test_remove_first_single_element():
    cll = CircularLinkedList()
    cll.add_last(42)

    value = cll.remove_first()
    assert value == 42
    assert cll.is_empty()
    assert len(cll) == 0
    assert repr(cll) == "CircularLinkedList([])"
    assert cll.tail is None


def test_remove_first_multiple_elements():
    cll = CircularLinkedList()
    cll.add_last(10)
    cll.add_last(20)
    cll.add_last(30)

    # list = [10, 20, 30]
    v1 = cll.remove_first()
    assert v1 == 10
    assert len(cll) == 2
    assert cll.get_first() == 20
    assert cll.get_last() == 30

    v2 = cll.remove_first()
    assert v2 == 20
    assert len(cll) == 1
    assert cll.get_first() == 30
    assert cll.get_last() == 30

    v3 = cll.remove_first()
    assert v3 == 30
    assert cll.is_empty()
    assert len(cll) == 0
    assert cll.tail is None


def test_remove_first_from_empty_raises():
    cll = CircularLinkedList()
    with pytest.raises(IndexError):
        cll.remove_first()


def test_get_first_and_last_from_empty_raises():
    cll = CircularLinkedList()

    with pytest.raises(IndexError):
        cll.get_first()

    with pytest.raises(IndexError):
        cll.get_last()


def test_find_existing_element():
    cll = CircularLinkedList()
    cll.add_last("a")
    cll.add_last("b")
    cll.add_last("c")

    node_b = cll.find("b")
    assert node_b is not None
    assert node_b.value == "b"

    node_c = cll.find("c")
    assert node_c is not None
    assert node_c.value == "c"


def test_find_non_existing_element():
    cll = CircularLinkedList()
    cll.add_last(1)
    cll.add_last(2)
    cll.add_last(3)

    node = cll.find(99)
    assert node is None


def test_circular_traversal_internals():
    cll = CircularLinkedList()
    cll.add_last(10)
    cll.add_last(20)
    cll.add_last(30)

    head = cll.tail.next
    current = head

    values = []
    for _ in range(len(cll)):
        values.append(current.value)
        current = current.next

    assert current is head
    assert values == [10, 20, 30]
