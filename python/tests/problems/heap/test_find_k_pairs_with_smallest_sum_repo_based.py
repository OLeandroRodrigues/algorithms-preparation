import pytest

from problems.heap.find_k_pairs_with_smallest_sum_repo_based import Solution
    
solution = Solution()
def test_basic_case():
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    expected = [(1, 2), (1, 4), (1, 6)]
    assert solution.find_k_pairs_with_smallest_sum_repo_based(nums1, nums2, k) == expected


def test_with_duplicates():
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 2
    result = solution.find_k_pairs_with_smallest_sum_repo_based(nums1, nums2, k)
    assert result == [(1, 1), (1, 1)]


def test_empty_inputs():
    assert solution.find_k_pairs_with_smallest_sum_repo_based([], [1, 2], 3) == []
    assert solution.find_k_pairs_with_smallest_sum_repo_based([1, 2], [], 3) == []
    assert solution.find_k_pairs_with_smallest_sum_repo_based([], [], 3) == []


def test_k_zero():
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert solution.find_k_pairs_with_smallest_sum_repo_based(nums1, nums2, 0) == []


def test_more_pairs_than_possible():
    nums1 = [1, 2]
    nums2 = [1, 2, 3]
    k = 10
    result = solution.find_k_pairs_with_smallest_sum_repo_based(nums1, nums2, k)
    # All possible pairs sorted by sum:
    expected = [(1, 1), (1, 2), (2, 1), (1, 3), (2, 2), (2, 3)]
    assert result == expected


def test_large_input_small_k():
    nums1 = list(range(1, 100))
    nums2 = list(range(100, 200))
    k = 5
    result = solution.find_k_pairs_with_smallest_sum_repo_based(nums1, nums2, k)
    # smallest sums will all come from nums1[0] + nums2[0..4]
    expected = [(1, 100), (1, 101), (1, 102), (1, 103), (1, 104)]
    assert result == expected