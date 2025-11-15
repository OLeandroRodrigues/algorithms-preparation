import pytest
from data_structures.linkedlist.doubly_linked_list.doubly_linked_list_scratch  import DoublyLinkedList, Node


class TestDoublyLinkedList:

    @pytest.fixture
    def lst(self):
        return DoublyLinkedList()

    # ---------- Estado inicial ----------
    def test_initial_state(self, lst):
        assert lst.is_empty()
        assert lst.size() == 0
        assert len(lst) == 0
        assert lst.head is None
        assert lst.tail is None

    # ---------- push_front ----------
    def test_push_front_empty(self, lst):
        n = lst.push_front(10)
        assert lst.head is n
        assert lst.tail is n
        assert lst.size() == 1

    def test_push_front_non_empty(self, lst):
        n1 = lst.push_front(10)
        n2 = lst.push_front(20)
        assert lst.head is n2
        assert lst.tail is n1
        assert list(lst) == [20, 10]

    # ---------- push_back ----------
    def test_push_back_empty(self, lst):
        n = lst.push_back(10)
        assert lst.head is n
        assert lst.tail is n
        assert lst.size() == 1

    def test_push_back_non_empty(self, lst):
        n1 = lst.push_back(10)
        n2 = lst.push_back(20)
        assert lst.head is n1
        assert lst.tail is n2
        assert list(lst) == [10, 20]

    # ---------- insert_after ----------
    def test_insert_after_middle(self, lst):
        n1 = lst.push_back(10)
        n2 = lst.push_back(20)
        lst.push_back(30)

        lst.insert_after(n1, 15)
        assert list(lst) == [10, 15, 20, 30]

    def test_insert_after_tail(self, lst):
        n1 = lst.push_back(10)
        n2 = lst.push_back(20)
        n3 = lst.insert_after(n2, 30)

        assert lst.tail is n3
        assert list(lst) == [10, 20, 30]

    def test_insert_after_none_raises(self, lst):
        with pytest.raises(ValueError):
            lst.insert_after(None, 10)

    # ---------- insert_before ----------
    def test_insert_before_middle(self, lst):
        lst.push_back(10)
        n2 = lst.push_back(20)
        lst.push_back(30)

        lst.insert_before(n2, 15)
        assert list(lst) == [10, 15, 20, 30]

    def test_insert_before_head(self, lst):
        n1 = lst.push_back(10)
        lst.push_back(20)

        lst.insert_before(n1, 5)
        assert lst.head.value == 5
        assert list(lst) == [5, 10, 20]

    def test_insert_before_none_raises(self, lst):
        with pytest.raises(ValueError):
            lst.insert_before(None, 10)

    # ---------- pop_front ----------
    def test_pop_front_single(self, lst):
        lst.push_back(10)
        assert lst.pop_front() == 10
        assert lst.is_empty()

    def test_pop_front_multiple(self, lst):
        lst.push_back(10)
        lst.push_back(20)
        assert lst.pop_front() == 10
        assert list(lst) == [20]

    def test_pop_front_empty_raises(self, lst):
        with pytest.raises(IndexError):
            lst.pop_front()

    # ---------- pop_back ----------
    def test_pop_back_single(self, lst):
        lst.push_back(10)
        assert lst.pop_back() == 10
        assert lst.is_empty()

    def test_pop_back_multiple(self, lst):
        lst.push_back(10)
        lst.push_back(20)
        assert lst.pop_back() == 20
        assert list(lst) == [10]

    def test_pop_back_empty_raises(self, lst):
        with pytest.raises(IndexError):
            lst.pop_back()

    # ---------- remove ----------
    def test_remove_single(self, lst):
        n = lst.push_back(10)
        assert lst.remove(n) == 10
        assert lst.is_empty()

    def test_remove_head(self, lst):
        n1 = lst.push_back(10)
        lst.push_back(20)
        lst.push_back(30)

        lst.remove(n1)
        assert list(lst) == [20, 30]
        assert lst.head.value == 20

    def test_remove_tail(self, lst):
        lst.push_back(10)
        lst.push_back(20)
        n3 = lst.push_back(30)

        lst.remove(n3)
        assert list(lst) == [10, 20]
        assert lst.tail.value == 20

    def test_remove_middle(self, lst):
        n1 = lst.push_back(10)
        n2 = lst.push_back(20)
        n3 = lst.push_back(30)

        lst.remove(n2)
        assert list(lst) == [10, 30]
        assert lst.head.next is n3

    def test_remove_none_raises(self, lst):
        with pytest.raises(ValueError):
            lst.remove(None)

    def test_remove_from_empty_raises(self):
        lst = DoublyLinkedList()
        with pytest.raises(IndexError):
            lst.remove(Node(10))

    # ---------- find ----------
    def test_find_existing(self, lst):
        lst.push_back(10)
        lst.push_back(20)
        lst.push_back(30)
        node = lst.find(20)
        assert node is not None
        assert node.value == 20

    def test_find_missing(self, lst):
        lst.push_back(10)
        lst.push_back(20)
        assert lst.find(99) is None

    # ---------- iter / repr ----------
    def test_iter_and_repr(self, lst):
        lst.push_back(1)
        lst.push_back(2)
        lst.push_back(3)

        assert list(lst) == [1, 2, 3]

        r = repr(lst)
        assert "DoublyLinkedList" in r
        assert "1" in r
        assert "2" in r
        assert "3" in r
