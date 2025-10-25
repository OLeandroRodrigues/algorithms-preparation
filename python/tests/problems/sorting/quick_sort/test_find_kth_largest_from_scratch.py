import pytest
from problems.sorting.quick_sort.find_kth_largest_from_scratch import findKthLargest


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        # Examples from LeetCode statement
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),

        # Small edge cases
        ([1], 1, 1),
        ([2, 1], 1, 2),
        ([2, 1], 2, 1),

        # With duplicates
        ([5, 5, 5, 5], 2, 5),
        ([2, 2, 1, 1, 3, 3], 3, 2),

        # With negatives
        ([-1, -5, 0, 2, -3], 1, 2),
        ([-1, -5, 0, 2, -3], 3, -1),

        # Already sorted ascending / descending
        ([1, 2, 3, 4, 5, 6], 2, 5),
        ([6, 5, 4, 3, 2, 1], 2, 5),

        # Larger mix
        ([10, 3, 7, 2, 9, 1, 5, 8, 6, 4], 5, 6),
    ]
)
def test_find_kth_largest(nums, k, expected):
    assert findKthLargest(nums[:], k) == expected


def test_matches_sorted_reference():
    data = [7, 2, 9, 4, 5]
    for k in range(1, len(data) + 1):
        expected = sorted(data)[-k]
        assert findKthLargest(data[:], k) == expected


def test_in_place_behavior():
    arr = [3, 2, 1]
    result = findKthLargest(arr, 1)
    assert result == 3
    # array should now be fully sorted in ascending order
    assert arr == [1, 2, 3]


def test_invalid_k_raises():
    with pytest.raises(IndexError):
        findKthLargest([1, 2, 3], 0)

    with pytest.raises(IndexError):
        findKthLargest([1, 2, 3], 10)