"""
Problem: Valid Anagram

Description:
Given two strings `s` and `t`, return True if `t` is an anagram of `s`,
and return False otherwise.

An anagram is formed by rearranging the letters of a string using all
the original characters exactly once.

Function Signature:
    def isAnagram(s: str, t: str) -> bool

Examples:
    Input: s = "anagram", t = "nagaram"
    Output: True

    Input: s = "rat", t = "car"
    Output: False

    Input: s = "aacc", t = "ccac"
    Output: False

Constraints:
    1 <= s.length, t.length <= 5 * 10^4
    s and t consist of lowercase English letters.

Expected Approach:
    - If lengths differ, return False immediately
    - Count character frequencies using a hash table or array
    - Compare frequencies of both strings

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(1) 
    (since the alphabet size is fixed: 26 lowercase letters)

Notes:
    - Sorting-based solutions are valid but less optimal (O(n log n)).
    - Hash-based counting is preferred for interview scenarios.
    - Early exit is encouraged when possible.
"""

class Solution:
   def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        hash_map_word_s = {}
        for letter in s:
            hash_map_word_s[letter] = hash_map_word_s.get(letter, 0) + 1
        
        hash_map_word_t = {}
        for letter in t:
            hash_map_word_t[letter] = hash_map_word_t.get(letter, 0) + 1
        
        for key, value in hash_map_word_s.items():
            if key not in hash_map_word_t or hash_map_word_t[key] != value:
                return False
        
        return True




