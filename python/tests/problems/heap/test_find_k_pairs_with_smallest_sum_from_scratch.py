import pytest
from problems.heap.find_k_pairs_with_smallest_sum_from_scratch import Solution


@pytest.mark.parametrize(
    "nums1, nums2, k, expected",
    [
        # Example 1
        ([1, 7, 11], [2, 4, 6], 3, [[1, 2], [1, 4], [1, 6]]),
        # Example 2
        ([1, 1, 2], [1, 2, 3], 2, [[1, 1], [1, 1]]),
        # Small mixed case
        ([1, 2], [3], 3, [[1, 3], [2, 3]]),
        # Larger range
        ([1, 2, 4, 5, 6], [3, 5, 7, 9], 3, [[1, 3], [2, 3], [1, 5]]),
        # Edge case: empty input
        ([], [1, 2, 3], 3, []),
        ([1, 2, 3], [], 3, []),
    ]
)
def test_k_smallest_pairs(nums1, nums2, k, expected):
    solution = Solution()
    result = solution.kSmallestPairs(nums1, nums2, k)

    # Since multiple valid orders can exist for equal sums, 
    # we sort for comparison to make test deterministic
    assert sorted(result) == sorted(expected)