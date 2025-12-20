"""
Problem: Find Word in Text (String Search)

Description:
Given a text string `text` and a pattern string `pattern` (a word),
return the index of the first occurrence of `pattern` in `text`.
If `pattern` does not occur in `text`, return -1.

This is a classic substring search problem (similar to strStr / indexOf).

Function Signature:
    def findWord(text: str, pattern: str) -> int

Examples:
    Input: text = "here is a simple example", pattern = "simple"
    Output: 10

    Input: text = "aaaaa", pattern = "bba"
    Output: -1

    Input: text = "abc", pattern = ""
    Output: 0

Constraints:
    0 <= text.length <= 10^5
    0 <= pattern.length <= 10^4
    text and pattern consist of ASCII characters (or lowercase English letters).

Expected Approach:
    - Brute force: check all possible alignments (O(n * m))
    - Efficient approaches:
        - Boyer–Moore (bad character + good suffix heuristics)
        - KMP (prefix function / LPS table)
        - Rabin–Karp (rolling hash)

Complexity:
    Brute force:
        Time Complexity: O(n * m)
        Space Complexity: O(1)

    Efficient (typical expectations):
        - KMP: Time O(n + m), Space O(m)
        - Boyer–Moore: Average sublinear, worst-case O(n + m)
        - Rabin–Karp: Average O(n + m), worst-case O(n * m)

Notes:
    - If `pattern` is empty, return 0 (common convention).
    - This problem is commonly used to test understanding of string matching
      algorithms and preprocessing techniques.
"""

from typing import Dict, List
class Solution:

    def _build_bad_character_table(self,pattern: str) -> Dict[str, int]:
        """
        last[c] = last index where character c appears in pattern, or -1 if absent.
        """
        last = {}
        for i, ch in enumerate(pattern):
            last[ch] = i
        return last


    def _build_good_suffix_table(self, pattern: str) -> List[int]:
        """
        Builds the good-suffix shift table using the classic Boyer–Moore preprocessing
        with border positions (a.k.a. strong good suffix rule).

        Returns:
            shift: list of length m+1 where shift[i] is the shift to apply when mismatch
                happens at pattern index i-1 (or when a match is found at i=0).
        """
        m = len(pattern)
        shift = [0] * (m + 1)
        bpos = [0] * (m + 1)

        # Step 1: compute border positions
        i = m
        j = m + 1
        bpos[i] = j

        while i > 0:
            while j <= m and pattern[i - 1] != pattern[j - 1]:
                if shift[j] == 0:
                    shift[j] = j - i
                j = bpos[j]
            i -= 1
            j -= 1
            bpos[i] = j

        # Step 2: fill remaining shifts using the widest border
        j = bpos[0]
        for i in range(m + 1):
            if shift[i] == 0:
                shift[i] = j
            if i == j:
                j = bpos[j]

        return shift


    def findWord(self, text: str, pattern: str) -> int:
        """
        Boyer–Moore string search (Bad Character + Good Suffix).
        Returns the index of the first occurrence of `pattern` in `text`, or -1.
        Convention: empty pattern -> 0.
        """
        n = len(text)
        m = len(pattern)

        if m == 0:
            return 0
        if m > n:
            return -1

        last = Solution()._build_bad_character_table(pattern)
        shift = Solution()._build_good_suffix_table(pattern)

        s = 0  # shift of the pattern over text
        while s <= n - m:
            j = m - 1

            # Compare from right to left
            while j >= 0 and pattern[j] == text[s + j]:
                j -= 1

            # Match found
            if j < 0:
                return s

            # Bad character rule:
            bad_char = text[s + j]
            last_pos = last.get(bad_char, -1)
            bc_shift = j - last_pos  # if last_pos == -1 => shift = j+1

            # Good suffix rule:
            gs_shift = shift[j + 1]  # j mismatch at pattern[j], so use j+1

            s += max(bc_shift, gs_shift)

        return -1 