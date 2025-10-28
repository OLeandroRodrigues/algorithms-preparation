import pytest
import random


from algorithms.sorting.quick_sort.randomized.quick_sort_randomized import quick_sort


@pytest.fixture(autouse=True)
def _seed_random():
    """
    Makes the tests reproducible even with a random pivot
    """
    random.seed(1337)


def _run_sort_in_place(arr):
    """
    Helper function to call quick_sort consistently:
    - ensures it returns None (in-place)
    - applies correct index boundaries
    - returns the array itself for convenient assertions
    """
    ret = quick_sort(arr, 0, len(arr) - 1) if arr else quick_sort(arr, 0, -1)
    assert ret is None  # quick_sort clássico costuma retornar None (in-place)
    return arr


def test_empty_list():
    arr = []
    assert _run_sort_in_place(arr) == []


def test_single_element():
    arr = [42]
    assert _run_sort_in_place(arr) == [42]


def test_sorted_list():
    arr = [1, 2, 3, 4, 5]
    assert _run_sort_in_place(arr) == [1, 2, 3, 4, 5]


def test_reverse_list():
    arr = [5, 4, 3, 2, 1]
    assert _run_sort_in_place(arr) == [1, 2, 3, 4, 5]


def test_unsorted_list():
    arr = [3, 1, 4, 1, 5, 9, 2]
    assert _run_sort_in_place(arr) == sorted(arr)


def test_with_duplicates():
    arr = [5, 3, 5, 2, 5, 1]
    assert _run_sort_in_place(arr) == sorted(arr)


def test_with_negative_numbers():
    arr = [0, -10, 5, -3, 2]
    assert _run_sort_in_place(arr) == sorted(arr)


@pytest.mark.parametrize("arr", [
    [],
    [1],
    [2, 1],
    [3, 1, 2],
    [10, -1, 7, 7, 3, 2, 100, 0],
    [5, 5, 5, 5],
    [9, -2, -2, 9, 0, 0, 3, -1],
])
def test_parametrized_cases(arr):
    expected = sorted(arr)
    got = _run_sort_in_place(arr.copy())
    assert got == expected


def test_in_place_behavior_and_return_none():
    arr = [2, 8, 7, 1, 3, 5, 6]
    ret = quick_sort(arr, 0, len(arr) - 1)
    assert ret is None
    assert arr == sorted([2, 8, 7, 1, 3, 5, 6])