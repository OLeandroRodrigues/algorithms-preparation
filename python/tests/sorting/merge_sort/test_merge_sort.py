# tests/sorting/merge_sort/test_merge_sort.py
import pytest
from algorithms.sorting.merge_sort import merge_sort

def test_empty_list():
    assert merge_sort([]) == [], "Sorting an empty list should return an empty list."

def test_single_element():
    assert merge_sort([42]) == [42]

def test_sorted_list():
    assert merge_sort([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_reverse_sorted_list():
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_unsorted_list():
    assert merge_sort([3, 1, 4, 2]) == [1, 2, 3, 4]

def test_list_with_duplicates():
    assert merge_sort([4, 2, 2, 3, 1]) == [1, 2, 2, 3, 4]

def test_list_with_negative_numbers():
    assert merge_sort([3, -1, -5, 2, 0]) == [-5, -1, 0, 2, 3]

def test_list_with_all_equal_elements():
    assert merge_sort([7, 7, 7, 7]) == [7, 7, 7, 7]

def test_large_list():
    arr = [10, 3, 7, 2, 9, 1, 5, 8, 6, 4]
    assert merge_sort(arr) == sorted(arr)