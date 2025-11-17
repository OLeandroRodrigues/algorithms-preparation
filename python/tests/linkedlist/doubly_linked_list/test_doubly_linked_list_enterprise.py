import pytest
from data_structures.linkedlist.doubly_linked_list.doubly_linked_list_enterprise  import DoublyLinkedList


class TestDoublyLinkedList:
    @pytest.fixture
    def empty_list(self) -> DoublyLinkedList[int]:
        return DoublyLinkedList[int]()

    @pytest.fixture
    def sample_list(self) -> DoublyLinkedList[int]:
        # lista: [1, 2, 3]
        return DoublyLinkedList([1, 2, 3])

    # ---------- initial state / construtor ----------

    def test_initial_state_empty(self, empty_list: DoublyLinkedList[int]) -> None:
        lst = empty_list
        assert lst.is_empty()
        assert lst.size() == 0
        assert len(lst) == 0
        assert bool(lst) is False
        assert lst.head is None
        assert lst.tail is None
        assert list(lst) == []

    def test_constructor_with_iterable(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list
        assert not lst.is_empty()
        assert lst.size() == 3
        assert list(lst) == [1, 2, 3]
        assert lst.head is not None
        assert lst.tail is not None
        assert lst.head.value == 1
        assert lst.tail.value == 3

    # ---------- push_front / push_back ----------

    def test_push_front_on_empty_list(self, empty_list: DoublyLinkedList[int]) -> None:
        lst = empty_list
        n = lst.push_front(10)

        assert not lst.is_empty()
        assert lst.size() == 1
        assert lst.head is n
        assert lst.tail is n
        assert n.prev is None
        assert n.next is None
        assert list(lst) == [10]

    def test_push_front_on_non_empty_list(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list    # [1, 2, 3]
        n = lst.push_front(0)

        assert lst.size() == 4
        assert lst.head is n
        assert n.value == 0
        assert n.prev is None
        assert n.next.value == 1
        assert list(lst) == [0, 1, 2, 3]

    def test_push_back_on_empty_list(self, empty_list: DoublyLinkedList[int]) -> None:
        lst = empty_list
        n = lst.push_back(10)

        assert not lst.is_empty()
        assert lst.size() == 1
        assert lst.head is n
        assert lst.tail is n
        assert n.prev is None
        assert n.next is None
        assert list(lst) == [10]

    def test_push_back_on_non_empty_list(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list    # [1, 2, 3]
        n = lst.push_back(4)

        assert lst.size() == 4
        assert lst.tail is n
        assert n.value == 4
        assert n.next is None
        assert n.prev.value == 3
        assert list(lst) == [1, 2, 3, 4]

    # ---------- insert_after / insert_before ----------

    def test_insert_after_middle_node(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list  # [1, 2, 3]
        node_1 = lst.head              # value 1
        assert node_1 is not None
        node_2 = node_1.next           # value 2
        assert node_2 is not None

        new_node = lst.insert_after(node_1, 1_5)  # [1, 1.5, 2, 3]

        assert lst.size() == 4
        assert node_1.next is new_node
        assert new_node.prev is node_1
        assert new_node.next is node_2
        assert node_2.prev is new_node
        assert list(lst) == [1, 1_5, 2, 3]

    def test_insert_after_tail_delegates_to_push_back(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list  # [1, 2, 3]
        tail = lst.tail
        assert tail is not None

        new_node = lst.insert_after(tail, 4)

        assert lst.tail is new_node
        assert lst.size() == 4
        assert list(lst) == [1, 2, 3, 4]

    def test_insert_after_none_raises(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list
        with pytest.raises(ValueError):
            lst.insert_after(None, 99)  # type: ignore[arg-type]

    def test_insert_before_middle_node(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list  # [1, 2, 3]
        node_2 = lst.head.next  # type: ignore[union-attr]
        assert node_2 is not None
        assert node_2.value == 2

        new_node = lst.insert_before(node_2, 1_5)

        assert lst.size() == 4
        assert new_node.next is node_2
        assert new_node.prev is not None
        assert new_node.prev.value == 1
        assert node_2.prev is new_node
        assert list(lst) == [1, 1_5, 2, 3]

    def test_insert_before_head_delegates_to_push_front(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list  # [1, 2, 3]
        head = lst.head
        assert head is not None

        new_node = lst.insert_before(head, 0)

        assert lst.head is new_node
        assert lst.size() == 4
        assert list(lst) == [0, 1, 2, 3]

    def test_insert_before_none_raises(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list
        with pytest.raises(ValueError):
            lst.insert_before(None, 99)  # type: ignore[arg-type]

    # ---------- pop_front / pop_back ----------

    def test_pop_front_single_element(self, empty_list: DoublyLinkedList[int]) -> None:
        lst = empty_list
        lst.push_back(10)

        value = lst.pop_front()
        assert value == 10
        assert lst.is_empty()
        assert lst.head is None
        assert lst.tail is None

    def test_pop_front_multiple_elements(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list  # [1, 2, 3]

        value = lst.pop_front()
        assert value == 1
        assert lst.size() == 2
        assert list(lst) == [2, 3]
        assert lst.head is not None
        assert lst.head.prev is None

    def test_pop_front_on_empty_list_raises(self, empty_list: DoublyLinkedList[int]) -> None:
        lst = empty_list
        with pytest.raises(IndexError):
            lst.pop_front()

    def test_pop_back_single_element(self, empty_list: DoublyLinkedList[int]) -> None:
        lst = empty_list
        lst.push_back(10)

        value = lst.pop_back()
        assert value == 10
        assert lst.is_empty()
        assert lst.head is None
        assert lst.tail is None

    def test_pop_back_multiple_elements(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list  # [1, 2, 3]

        value = lst.pop_back()
        assert value == 3
        assert lst.size() == 2
        assert list(lst) == [1, 2]
        assert lst.tail is not None
        assert lst.tail.next is None

    def test_pop_back_on_empty_list_raises(self, empty_list: DoublyLinkedList[int]) -> None:
        lst = empty_list
        with pytest.raises(IndexError):
            lst.pop_back()

    # ---------- remove(node) ----------

    def test_remove_single_node(self, empty_list: DoublyLinkedList[int]) -> None:
        lst = empty_list
        node = lst.push_back(10)

        removed = lst.remove(node)
        assert removed == 10
        assert lst.is_empty()
        assert lst.head is None
        assert lst.tail is None

    def test_remove_head_in_multi_element_list(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list  # [1, 2, 3]
        head = lst.head
        assert head is not None

        removed = lst.remove(head)
        assert removed == 1
        assert lst.size() == 2
        assert list(lst) == [2, 3]
        assert lst.head is not None
        assert lst.head.prev is None

    def test_remove_tail_in_multi_element_list(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list  # [1, 2, 3]
        tail = lst.tail
        assert tail is not None

        removed = lst.remove(tail)
        assert removed == 3
        assert lst.size() == 2
        assert list(lst) == [1, 2]
        assert lst.tail is not None
        assert lst.tail.next is None

    def test_remove_middle_node(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list  # [1, 2, 3]
        middle = lst.head.next  # type: ignore[union-attr]
        assert middle is not None
        assert middle.value == 2

        removed = lst.remove(middle)
        assert removed == 2
        assert lst.size() == 2
        assert list(lst) == [1, 3]

        head = lst.head
        tail = lst.tail
        assert head is not None and tail is not None
        assert head.next is tail
        assert tail.prev is head

    def test_remove_none_raises(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list
        with pytest.raises(ValueError):
            lst.remove(None)  # type: ignore[arg-type]

    def test_remove_from_empty_list_raises(self, empty_list: DoublyLinkedList[int]) -> None:
        lst = empty_list
        # cria um nó “fake” via push_back e depois limpa
        node = lst.push_back(10)
        lst.clear()
        with pytest.raises(IndexError):
            lst.remove(node)

    # ---------- find / clear ----------

    def test_find_existing_value(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list  # [1, 2, 3]
        node = lst.find(2)
        assert node is not None
        assert node.value == 2

    def test_find_missing_value(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list
        node = lst.find(99)
        assert node is None

    def test_clear_empties_list(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list
        lst.clear()

        assert lst.is_empty()
        assert lst.size() == 0
        assert lst.head is None
        assert lst.tail is None
        assert list(lst) == []

    # ---------- iter / reversed / contains / repr ----------

    def test_iter(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list
        assert list(lst) == [1, 2, 3]

    def test_reversed(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list
        assert list(reversed(lst)) == [3, 2, 1]

    def test_contains(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list
        assert 1 in lst
        assert 2 in lst
        assert 3 in lst
        assert 99 not in lst

    def test_repr(self, sample_list: DoublyLinkedList[int]) -> None:
        lst = sample_list
        r = repr(lst)
        assert "DoublyLinkedList" in r
        assert "1" in r
        assert "2" in r
        assert "3" in r
