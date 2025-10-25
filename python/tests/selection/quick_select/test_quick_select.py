import pytest
from algorithms.selection.quick_select import quick_select


def test_single_element():
    arr = [42]
    k = 1
    assert quick_select(arr, 0, len(arr) - 1, k) == 42


def test_sorted_list():
    arr = [1, 2, 3, 4, 5]
    assert quick_select(arr.copy(), 0, len(arr) - 1, 1) == 1  # smallest
    assert quick_select(arr.copy(), 0, len(arr) - 1, 3) == 3  # middle
    assert quick_select(arr.copy(), 0, len(arr) - 1, 5) == 5  # largest


def test_reverse_sorted_list():
    arr = [5, 4, 3, 2, 1]
    assert quick_select(arr.copy(), 0, len(arr) - 1, 1) == 1
    assert quick_select(arr.copy(), 0, len(arr) - 1, 3) == 3
    assert quick_select(arr.copy(), 0, len(arr) - 1, 5) == 5


def test_unsorted_list():
    arr = [7, 10, 4, 3, 20, 15]
    assert quick_select(arr.copy(), 0, len(arr) - 1, 1) == 3
    assert quick_select(arr.copy(), 0, len(arr) - 1, 3) == 7
    assert quick_select(arr.copy(), 0, len(arr) - 1, 6) == 20


def test_with_duplicates():
    arr = [5, 3, 5, 2, 5, 1]
    assert quick_select(arr.copy(), 0, len(arr) - 1, 1) == 1
    assert quick_select(arr.copy(), 0, len(arr) - 1, 3) == 3 
    assert quick_select(arr.copy(), 0, len(arr) - 1, 6) == 5


def test_with_negative_numbers():
    arr = [0, -10, 5, -3, 2]
    assert quick_select(arr.copy(), 0, len(arr) - 1, 1) == -10
    assert quick_select(arr.copy(), 0, len(arr) - 1, 3) == 0
    assert quick_select(arr.copy(), 0, len(arr) - 1, 5) == 5


def test_invalid_k_values():
    arr = [3, 1, 4]
    with pytest.raises(IndexError):
        quick_select(arr, 0, len(arr) - 1, 0)
    with pytest.raises(IndexError):
        quick_select(arr, 0, len(arr) - 1, 5)


@pytest.mark.parametrize("arr,k,expected", [
    ([1], 1, 1),
    ([2, 1], 1, 1),
    ([3, 1, 2], 2, 2),
    ([10, -1, 7, 7, 3, 2, 100, 0], 4, 3),
    ([10, -1, 7, 7, 3, 2, 100, 0], 8, 100),
])
def test_parametrized_cases(arr, k, expected):
    assert quick_select(arr.copy(), 0, len(arr) - 1, k) == expected