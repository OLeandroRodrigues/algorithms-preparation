# tests/heap/min_heap/test_min_heap.py
import pytest
from data_structures.heap.min_heap import MinHeap


def test_empty_heap_pop():
    h = MinHeap()
    with pytest.raises(IndexError):
        h.pop()


def test_single_element_insert_pop():
    h = MinHeap()
    h.insert(42)
    assert h.pop() == 42
    assert h._data == []


def test_heap_property_after_inserts():
    h = MinHeap()
    for v in [3, 1, 6, 5, 2, 4]:
        h.insert(v)
    # the smallest must be in the root
    assert h._data[0] == min([3, 1, 6, 5, 2, 4])


def test_pop_returns_sorted_asc():
    h = MinHeap()
    values = [5, 1, 9, 2, 8, 3, 7]
    for v in values:
        h.insert(v)
    popped = [h.pop() for _ in range(len(values))]
    assert popped == sorted(values)


def test_with_duplicates():
    h = MinHeap()
    values = [5, 3, 5, 2, 5, 1]
    for v in values:
        h.insert(v)
    popped = [h.pop() for _ in range(len(values))]
    assert popped == sorted(values)


def test_with_negative_numbers():
    h = MinHeap()
    values = [0, -10, 5, -3, 2]
    for v in values:
        h.insert(v)
    popped = [h.pop() for _ in range(len(values))]
    assert popped == sorted(values)


@pytest.mark.parametrize("arr", [
    [],
    [1],
    [2, 1],
    [3, 1, 2],
    [10, -1, 7, 7, 3, 2, 100, 0],
])
def test_parametrized_cases(arr):
    h = MinHeap()
    for v in arr:
        h.insert(v)
    popped = [h.pop() for _ in range(len(arr))]
    assert popped == sorted(arr)