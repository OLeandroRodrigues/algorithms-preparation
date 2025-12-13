import pytest
from problems.binary_search.binary_search_find_index import Solution


def test_target_found_middle():
    sol = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    assert sol.search(nums, target) == 4


def test_target_not_found():
    sol = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2

    assert sol.search(nums, target) == -1


def test_single_element_found():
    sol = Solution()
    nums = [5]
    target = 5

    assert sol.search(nums, target) == 0


def test_single_element_not_found():
    sol = Solution()
    nums = [5]
    target = 3

    assert sol.search(nums, target) == -1


def test_target_at_beginning():
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    target = 1

    assert sol.search(nums, target) == 0


def test_target_at_end():
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    target = 5

    assert sol.search(nums, target) == 4