
import pytest
import random
from problems.selection.quick_select.find_kth_largest_from_scratch_v2 import quick_select

def find_kth_largest(nums, k):
    """Wrapper to use quick_select to find the k-th largest element."""
    n = len(nums)
    # kth largest == (n - k + 1)-th smallest
    
    return quick_select(nums, 0, n - 1, n - k + 1)


class TestKthLargest:
    def test_example_1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        result = find_kth_largest(nums, k)
        assert result == 5

    def test_example_2(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        result = find_kth_largest(nums, k)
        assert result == 4

    def test_with_duplicates(self):
        nums = [4, 4, 4, 4, 4]
        k = 3
        result = find_kth_largest(nums, k)
        assert result == 4

    def test_with_negative_numbers(self):
        nums = [-1, -5, -3, -4, -2]
        k = 2
        result = find_kth_largest(nums, k)
        assert result == -2

    def test_single_element(self):
        nums = [42]
        k = 1
        result = find_kth_largest(nums, k)
        assert result == 42

    def test_sorted_descending(self):
        nums = [9, 8, 7, 6, 5]
        k = 3
        result = find_kth_largest(nums, k)
        assert result == 7

    def test_sorted_ascending(self):
        nums = [1, 2, 3, 4, 5]
        k = 2
        result = find_kth_largest(nums, k)
        assert result == 4

    def test_random_large_array(self):
        nums = random.sample(range(1, 1001), 1000)
        k = 100
        result = find_kth_largest(nums, k)
        expected = sorted(nums, reverse=True)[k - 1]
        assert result == expected

    def test_invalid_k_raises(self):
        nums = [1, 2, 3]
        with pytest.raises(IndexError):
            find_kth_largest(nums, 0)
        with pytest.raises(IndexError):
            find_kth_largest(nums, 10)
