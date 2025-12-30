import pytest
from problems.arrays.find_maximum_subarray import Solution


class TestMaximumSubarray:

    def setup_method(self):
        self.solution = Solution()

    def test_example_case(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        assert self.solution.maxSubArray(nums) == 6

    def test_single_element_positive(self):
        nums = [5]
        assert self.solution.maxSubArray(nums) == 5

    def test_single_element_negative(self):
        nums = [-7]
        assert self.solution.maxSubArray(nums) == -7

    def test_all_positive_numbers(self):
        nums = [1, 2, 3, 4]
        assert self.solution.maxSubArray(nums) == 10

    def test_all_negative_numbers(self):
        nums = [-8, -3, -6, -2, -5, -4]
        assert self.solution.maxSubArray(nums) == -2

    def test_mixed_numbers_with_max_in_middle(self):
        nums = [4, -1, 2, 1]
        assert self.solution.maxSubArray(nums) == 6

    def test_max_subarray_at_beginning(self):
        nums = [5, 4, -1, -2]
        assert self.solution.maxSubArray(nums) == 9

    def test_max_subarray_at_end(self):
        nums = [-3, -2, 4, 5]
        assert self.solution.maxSubArray(nums) == 9

    def test_with_zeros(self):
        nums = [0, -1, 2, 0, 3, -2]
        assert self.solution.maxSubArray(nums) == 5
