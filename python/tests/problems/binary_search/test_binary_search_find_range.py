import pytest
from problems.binary_search.binary_search_find_range import Solution


def test_target_with_multiple_occurrences():
    sol = Solution()
    nums = [1, 2, 4, 4, 4, 5]
    target = 4

    assert sol.searchRange(nums, target) == [2, 4]


def test_target_single_occurrence():
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    target = 3

    assert sol.searchRange(nums, target) == [2, 2]


def test_target_not_found():
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    target = 10

    assert sol.searchRange(nums, target) == [-1, -1]


def test_target_at_beginning():
    sol = Solution()
    nums = [2, 2, 2, 3, 4]
    target = 2

    assert sol.searchRange(nums, target) == [0, 2]


def test_target_at_end():
    sol = Solution()
    nums = [1, 2, 3, 4, 4, 4]
    target = 4

    assert sol.searchRange(nums, target) == [3, 5]


def test_single_element_found():
    sol = Solution()
    nums = [7]
    target = 7

    assert sol.searchRange(nums, target) == [0, 0]


def test_single_element_not_found():
    sol = Solution()
    nums = [7]
    target = 3

    assert sol.searchRange(nums, target) == [-1, -1]


def test_all_elements_same_and_equal_to_target():
    sol = Solution()
    nums = [5, 5, 5, 5]
    target = 5

    assert sol.searchRange(nums, target) == [0, 3]


def test_all_elements_same_and_not_equal_to_target():
    sol = Solution()
    nums = [5, 5, 5, 5]
    target = 1

    assert sol.searchRange(nums, target) == [-1, -1]


def test_empty_array():
    sol = Solution()
    nums = []
    target = 3

    assert sol.searchRange(nums, target) == [-1, -1]
