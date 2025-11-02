import pytest
from algorithms.sorting.counting_sort.counting_sort import counting_sort


def test_basic_unsorted_array():
    # General case from the example
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert counting_sort(arr) == [1, 2, 2, 3, 3, 4, 8]


def test_already_sorted_array():
    arr = [1, 2, 3, 4, 5]
    assert counting_sort(arr) == [1, 2, 3, 4, 5]


def test_reverse_sorted_array():
    arr = [5, 4, 3, 2, 1]
    assert counting_sort(arr) == [1, 2, 3, 4, 5]


def test_array_with_duplicates():
    arr = [5, 5, 5, 2, 2, 9, 9, 1]
    assert counting_sort(arr) == [1, 2, 2, 5, 5, 5, 9, 9]


def test_array_all_equal_values():
    arr = [7, 7, 7, 7]
    assert counting_sort(arr) == [7, 7, 7, 7]


def test_empty_array_returns_empty_list():
    arr = []
    assert counting_sort(arr) == []


def test_array_with_zero_included():
    arr = [0, 5, 0, 3, 2, 2]
    assert counting_sort(arr) == [0, 0, 2, 2, 3, 5]


def test_large_values_still_sort_correctly():
    arr = [100, 1, 50, 50, 100, 0]
    assert counting_sort(arr) == [0, 1, 50, 50, 100, 100]


def test_stability_for_equal_numbers_by_value():
    arr = [2, 2, 2, 1, 1, 0, 0]
    assert counting_sort(arr) == [0, 0, 1, 1, 2, 2, 2]


def test_single_element_array():
    arr = [42]
    assert counting_sort(arr) == [42]


def test_big_random_like_distribution():
    arr = [3, 1, 2, 1, 0, 3, 2, 1, 0, 2]
    assert counting_sort(arr) == [0, 0, 1, 1, 1, 2, 2, 2, 3, 3]


def test_does_not_modify_input():
    arr = [4, 1, 4, 3]
    original_copy = arr.copy()
    counting_sort(arr)
    assert arr == original_copy