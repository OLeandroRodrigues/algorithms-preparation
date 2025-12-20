import pytest
from problems.boyer_moore.majority_vote.majority_element import Solution


def test_majority_element_basic_case():
    nums = [3, 2, 3]
    assert Solution.majorityElement(nums) == 3


def test_majority_element_multiple_occurrences():
    nums = [2, 2, 1, 1, 1, 2, 2]
    assert Solution.majorityElement(nums) == 2


def test_majority_element_single_element():
    nums = [1]
    assert Solution.majorityElement(nums) == 1


def test_majority_element_all_same():
    nums = [5, 5, 5, 5]
    assert Solution.majorityElement(nums) == 5


def test_majority_element_negative_numbers():
    nums = [-1, -1, -1, 2, 2]
    assert Solution.majorityElement(nums) == -1


def test_majority_element_large_input():
    nums = [10] * 10001 + [5] * 5000
    assert Solution.majorityElement(nums) == 10
