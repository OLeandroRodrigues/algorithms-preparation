# tests/sorting/insertion_sort/test_insertion_sort.py
import pytest
from algorithms.sorting.insertion_sort import insertion_sort

def test_empty_list():
    assert insertion_sort([]) == [], "Sorting an empty list should return an empty list."

def test_single_element():
    assert insertion_sort([42]) == [42]

def test_sorted_list():
    arr = [1, 2, 3, 4, 5]
    assert insertion_sort(arr[:]) == sorted(arr)

def test_reverse_list():
    arr = [5, 4, 3, 2, 1]
    assert insertion_sort(arr[:]) == sorted(arr)

def test_unsorted_list():
    arr = [3, 1, 4, 1, 5, 9, 2]
    assert insertion_sort(arr[:]) == sorted(arr)

def test_with_duplicates():
    arr = [5, 3, 5, 2, 5, 1]
    assert insertion_sort(arr[:]) == sorted(arr)

def test_with_negative_numbers():
    arr = [0, -10, 5, -3, 2]
    assert insertion_sort(arr[:]) == sorted(arr)

@pytest.mark.parametrize("arr", [
    [],
    [1],
    [2, 1],
    [3, 1, 2],
    [10, -1, 7, 7, 3, 2, 100, 0],
])
def test_parametrized_cases(arr):
    assert insertion_sort(arr[:]) == sorted(arr)