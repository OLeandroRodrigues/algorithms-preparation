# tests/sorting/heap_sort/test_heap_sort_inplace.py
import pytest
from algorithms.sorting.heap_sort.heap_sort_inplace import heap_sort

def test_empty_list():
    arr = []
    heap_sort(arr)
    assert arr == [], "Sorting an empty list should return an empty list."

def test_single_element():
    arr = [42]
    heap_sort(arr)
    assert arr == [42]

def test_sorted_list():
    arr = [1, 2, 3, 4, 5]
    heap_sort(arr)
    assert arr == sorted(arr)

def test_reverse_list():
    arr = [5, 4, 3, 2, 1]
    heap_sort(arr)
    assert arr == sorted(arr)

def test_unsorted_list():
    arr = [3, 1, 4, 1, 5, 9, 2]
    heap_sort(arr)
    assert arr == sorted(arr)

def test_with_duplicates():
    arr = [5, 3, 5, 2, 5, 1]
    heap_sort(arr)
    assert arr == sorted(arr)

def test_with_negative_numbers():
    arr = [0, -10, 5, -3, 2]
    heap_sort(arr)
    assert arr == sorted(arr)

@pytest.mark.parametrize("arr", [
    [],
    [1],
    [2, 1],
    [3, 1, 2],
    [10, -1, 7, 7, 3, 2, 100, 0],
])
def test_parametrized_cases(arr):
    original = arr[:]
    heap_sort(arr)
    assert arr == sorted(original)