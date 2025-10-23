import pytest
from algorithms.sorting.quick_sort import quick_sort

def run_quick_sort(arr):
    quick_sort(arr, 0, len(arr) - 1)
    return arr

def test_empty_list():
    arr = []
    assert run_quick_sort(arr) == [], "Sorting an empty list should return an empty list."


def test_single_element():
    arr = [42]
    assert run_quick_sort(arr) == [42]


def test_sorted_list():
    arr = [1, 2, 3, 4]
    assert run_quick_sort(arr) == [1, 2, 3, 4]


def test_reverse_sorted_list():
    arr = [5, 4, 3, 2, 1]
    assert run_quick_sort(arr) == [1, 2, 3, 4, 5]


def test_unsorted_list():
    arr = [3, 1, 4, 2]
    assert run_quick_sort(arr) == [1, 2, 3, 4]


def test_list_with_duplicates():
    arr = [4, 2, 2, 3, 1]
    assert run_quick_sort(arr) == [1, 2, 2, 3, 4]


def test_list_with_negative_numbers():
    arr = [3, -1, -5, 2, 0]
    assert run_quick_sort(arr) == [-5, -1, 0, 2, 3]


def test_list_with_all_equal_elements():
    arr = [7, 7, 7, 7]
    assert run_quick_sort(arr) == [7, 7, 7, 7]


def test_large_list():
    arr = [10, 3, 7, 2, 9, 1, 5, 8, 6, 4]
    expected = sorted(arr)
    assert run_quick_sort(arr) == expected


def test_list_with_mixed_signs_and_duplicates():
    arr = [0, -1, 5, -1, 3, 0, 2]
    expected = sorted(arr)
    assert run_quick_sort(arr) == expected