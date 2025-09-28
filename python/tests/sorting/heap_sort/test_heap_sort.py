# tests/sorting/heap_sort/test_heap_sort.py
import pytest
from algorithms.sorting.heap_sort.heap_sort import HeapSort

def test_empty_list():
    arr = []
    assert HeapSort.sort_asc(arr) == []
    assert HeapSort.sort_desc(arr) == []

def test_single_element():
    arr = [42]
    assert HeapSort.sort_asc(arr) == [42]
    assert HeapSort.sort_desc(arr) == [42]

def test_sorted_list():
    arr = [1, 2, 3, 4, 5]
    assert HeapSort.sort_asc(arr) == [1, 2, 3, 4, 5]
    assert HeapSort.sort_desc(arr) == [5, 4, 3, 2, 1]

def test_reverse_list():
    arr = [5, 4, 3, 2, 1]
    assert HeapSort.sort_asc(arr) == [1, 2, 3, 4, 5]
    assert HeapSort.sort_desc(arr) == [5, 4, 3, 2, 1]

def test_unsorted_list():
    arr = [3, 1, 4, 1, 5, 9, 2]
    assert HeapSort.sort_asc(arr) == sorted(arr)
    assert HeapSort.sort_desc(arr) == sorted(arr, reverse=True)

def test_with_duplicates():
    arr = [5, 3, 5, 2, 5, 1]
    assert HeapSort.sort_asc(arr) == sorted(arr)
    assert HeapSort.sort_desc(arr) == sorted(arr, reverse=True)

def test_with_negative_numbers():
    arr = [0, -10, 5, -3, 2]
    assert HeapSort.sort_asc(arr) == sorted(arr)
    assert HeapSort.sort_desc(arr) == sorted(arr, reverse=True)

@pytest.mark.parametrize("arr", [
    [],
    [1],
    [2, 1],
    [3, 1, 2],
    [10, -1, 7, 7, 3, 2, 100, 0],
])
def test_parametrized_cases(arr):
    assert HeapSort.sort_asc(arr) == sorted(arr)
    assert HeapSort.sort_desc(arr) == sorted(arr, reverse=True)