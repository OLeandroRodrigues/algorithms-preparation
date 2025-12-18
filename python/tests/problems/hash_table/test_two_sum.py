import pytest
from problems.hash_table.two_sum import Solution


def test_two_sum_basic_case():
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9

    result = sol.twoSum(nums, target)

    assert result == [0, 1] or result == [1, 0]


def test_two_sum_with_duplicates():
    sol = Solution()
    nums = [3, 3]
    target = 6

    result = sol.twoSum(nums, target)

    assert sorted(result) == [0, 1]


def test_two_sum_negative_numbers():
    sol = Solution()
    nums = [-3, 4, 3, 90]
    target = 0

    result = sol.twoSum(nums, target)

    assert sorted(result) == [0, 2]


def test_two_sum_zero():
    sol = Solution()
    nums = [0, 4, 3, 0]
    target = 0

    result = sol.twoSum(nums, target)

    assert sorted(result) == [0, 3]


def test_two_sum_large_numbers():
    sol = Solution()
    nums = [10**9, 3, -10**9]
    target = 0

    result = sol.twoSum(nums, target)

    assert sorted(result) == [0, 2]
