"""
Problem: Valid Palindrome
Pattern: Two Pointers (left / right)

Description:
Given a string s, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

Example:
Input:  "A man, a plan, a canal: Panama"
Output: True

------------------------------------------------------------
Approach:
Use two pointers starting from both ends of the string.
Move pointers inward, skipping non-alphanumeric characters,
and compare characters in a case-insensitive way.

Invariant:
- All characters outside the interval [left, right]
  have already been validated as matching.
- left and right always point to characters that are
  candidates for comparison (alphanumeric).

------------------------------------------------------------
Algorithm:
1. Initialize left = 0, right = len(s) - 1
2. While left < right:
   - Skip non-alphanumeric characters
   - Compare s[left] and s[right] (lowercased)
   - If mismatch, return False
   - Move both pointers inward
3. Return True if no mismatches are found

------------------------------------------------------------
Complexity:
Time:  O(n)
Space: O(1)
------------------------------------------------------------
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            # Compare characters ignoring case
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers inward
            left += 1
            right -= 1

        return True