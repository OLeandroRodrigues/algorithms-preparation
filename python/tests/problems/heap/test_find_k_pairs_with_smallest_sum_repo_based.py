import pytest

from problems.heap.find_k_pairs_with_smallest_sum_repo_based import find_k_pairs_with_smallest_sum_repo_based
    
    
def test_basic_case():

    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    expected = [(1, 2), (1, 4), (1, 6)]
    assert find_k_pairs_with_smallest_sum_repo_based(nums1, nums2, k) == expected


def test_with_duplicates():
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 2
    result = find_k_pairs_with_smallest_sum_repo_based(nums1, nums2, k)
    assert result == [(1, 1), (1, 1)]


def test_empty_inputs():
    assert find_k_pairs_with_smallest_sum_repo_based([], [1, 2], 3) == []
    assert find_k_pairs_with_smallest_sum_repo_based([1, 2], [], 3) == []
    assert find_k_pairs_with_smallest_sum_repo_based([], [], 3) == []


def test_k_zero():
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert find_k_pairs_with_smallest_sum_repo_based(nums1, nums2, 0) == []


def test_more_pairs_than_possible():
    nums1 = [1, 2]
    nums2 = [1, 2, 3]
    k = 10
    result = find_k_pairs_with_smallest_sum_repo_based(nums1, nums2, k)
    # All possible pairs sorted by sum:
    expected = [(1, 1), (1, 2), (2, 1), (1, 3), (2, 2), (2, 3)]
    assert result == expected


def test_large_input_small_k():
    nums1 = list(range(1, 100))
    nums2 = list(range(100, 200))
    k = 5
    result = find_k_pairs_with_smallest_sum_repo_based(nums1, nums2, k)
    # Smallest sums (with tie-breaking by (u, v)):
    expected = [(1, 100), (1, 101), (2, 100), (1, 102), (2, 101)]
    assert result == expected


def test_ordering_and_stability():
    nums1 = [1, 2, 3]
    nums2 = [1, 2]
    k = 4
    result = find_k_pairs_with_smallest_sum_repo_based(nums1, nums2, k)
    # Expected pairs sorted by sum ascending:
    expected = [(1, 1), (1, 2), (2, 1), (2, 2)]
    assert result == expected