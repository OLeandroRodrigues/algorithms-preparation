import pytest
from problems.binary_search.binary_search_closest_element import Solution


def test_exact_match():
    sol = Solution()
    nums = [1, 3, 5, 8, 10]
    assert sol.closest_value(nums, 8) == 3


def test_between_two_values_choose_closest_left():
    sol = Solution()
    nums = [1, 3, 5, 8, 10]
    # target=7 is closer to 8 than 5 -> index 3
    assert sol.closest_value(nums, 7) == 3


def test_between_two_values_choose_closest_right():
    sol = Solution()
    nums = [1, 3, 5, 8, 10]
    # target=6 is closer to 5 than 8 -> index 2
    assert sol.closest_value(nums, 6) == 2


def test_below_min_returns_zero():
    sol = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    assert sol.closest_value(nums, -10) == 0


def test_above_max_returns_last():
    sol = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    assert sol.closest_value(nums, 100) == len(nums) - 1


def test_tie_returns_smaller_index():
    sol = Solution()
    nums = [1, 4, 7, 10]
    # target=5 is equally close to 4 and 7 -> return index of 4 (1)
    assert sol.closest_value(nums, 5) == 1


def test_single_element():
    sol = Solution()
    nums = [42]
    assert sol.closest_value(nums, 100) == 0
    assert sol.closest_value(nums, 42) == 0
    assert sol.closest_value(nums, -100) == 0


def test_empty_array_raises():
    sol = Solution()
    with pytest.raises(ValueError):
        sol.closest_value([], 10)
