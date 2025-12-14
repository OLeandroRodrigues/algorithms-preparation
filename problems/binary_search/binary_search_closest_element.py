from typing import List


class Solution:
    def closest_value(self, nums: List[int], target: int) -> int:
        """
        Returns the index of the element closest to target.
        Tie-break: return the smaller index.
        Assumes nums is non-empty and sorted ascending.
        """
        n = len(nums)
        if n == 0:
            raise ValueError("nums must be non-empty")

        # If target is outside bounds, closest is at the edges
        if target <= nums[0]:
            return 0
        if target >= nums[-1]:
            return n - 1

        left, right = 0, n - 1

        # Find the first index i such that nums[i] >= target (lower_bound)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # Now left is the insertion position (first >= target)
        # Candidates are left-1 and left
        i = left
        j = left - 1

        # Compare distances
        if abs(nums[j] - target) <= abs(nums[i] - target):
            return j  # tie goes to left (smaller index)
        return i
