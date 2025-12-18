import pytest
from problems.hash_table.contains_duplicate import Solution


def test_contains_duplicate_true_basic():
    sol = Solution()
    nums = [1, 2, 3, 1]
    assert sol.containsDuplicate(nums) is True


def test_contains_duplicate_false_basic():
    sol = Solution()
    nums = [1, 2, 3, 4]
    assert sol.containsDuplicate(nums) is False


def test_contains_duplicate_true_multiple_duplicates():
    sol = Solution()
    nums = [1, 1, 1, 3, 3, 4]
    assert sol.containsDuplicate(nums) is True


def test_contains_duplicate_single_element():
    sol = Solution()
    nums = [42]
    assert sol.containsDuplicate(nums) is False


def test_contains_duplicate_with_negative_numbers():
    sol = Solution()
    nums = [-1, -2, -3, -1]
    assert sol.containsDuplicate(nums) is True


def test_contains_duplicate_with_zeros():
    sol = Solution()
    nums = [0, 1, 0]
    assert sol.containsDuplicate(nums) is True


def test_contains_duplicate_large_values():
    sol = Solution()
    nums = [10**9, -10**9, 5, 10**9]
    assert sol.containsDuplicate(nums) is True
