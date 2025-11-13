import pytest
from data_structures.linkedlist.singly_linked_list_scratch import SinglyLinkedListScratch


class TestSinglyLinkedListScratch:
    
    def test_push_front(self):
        lst = SinglyLinkedListScratch()

        lst.push_front(3)   # [3]
        lst.push_front(2)   # [2, 3]
        lst.push_front(1)   # [1, 2, 3]

        assert lst.size() == 3
        assert lst.head.value == 1
        assert lst.head.next.value == 2
        assert lst.tail.value == 3

    def test_push_back(self):
        lst = SinglyLinkedListScratch()

        lst.push_back(1)    # [1]
        lst.push_back(2)    # [1, 2]
        lst.push_back(3)    # [1, 2, 3]

        assert lst.size() == 3
        assert lst.head.value == 1
        assert lst.tail.value == 3
        assert lst.head.next.value == 2

    def test_insert_after(self):
        lst = SinglyLinkedListScratch()

        n1 = lst.push_back(1)
        n2 = lst.push_back(2)
        lst.push_back(4)

        lst.insert_after(n2, 3)   # [1, 2, 3, 4]

        assert lst.size() == 4
        assert n2.next.value == 3
        assert n2.next.next.value == 4

    def test_pop_front(self):
        lst = SinglyLinkedListScratch()
        lst.push_back(10)
        lst.push_back(20)
        lst.push_back(30)

        value = lst.pop_front()   # removes 10

        assert value == 10
        assert lst.size() == 2
        assert lst.head.value == 20

    def test_pop_front_empty(self):
        lst = SinglyLinkedListScratch()

        with pytest.raises(IndexError):
            lst.pop_front()

    def test_remove_after(self):
        lst = SinglyLinkedListScratch()

        n1 = lst.push_back(1)
        n2 = lst.push_back(2)
        lst.push_back(3)

        removed = lst.remove_after(n1)  # removes 2

        assert removed == 2
        assert lst.size() == 2
        assert lst.head.next.value == 3
        assert lst.tail.value == 3

    def test_remove_after_invalid(self):
        lst = SinglyLinkedListScratch()

        n1 = lst.push_back(1)

        with pytest.raises(ValueError):
            lst.remove_after(n1)

    def test_find(self):
        lst = SinglyLinkedListScratch()
        lst.push_back("A")
        lst.push_back("B")
        lst.push_back("C")

        found = lst.find("B")
        assert found is not None
        assert found.value == "B"

        not_found = lst.find("X")
        assert not_found is None

    def test_is_empty_and_size(self):
        lst = SinglyLinkedListScratch()

        assert lst.is_empty() is True
        assert lst.size() == 0

        lst.push_back(1)

        assert lst.is_empty() is False
        assert lst.size() == 1