import pytest
from problems.hash_table.valid_anagram import Solution


def test_valid_anagram_true_basic():
    sol = Solution()
    s = "anagram"
    t = "nagaram"

    assert sol.isAnagram(s, t) is True


def test_valid_anagram_false_basic():
    sol = Solution()
    s = "rat"
    t = "car"

    assert sol.isAnagram(s, t) is False


def test_valid_anagram_different_lengths():
    sol = Solution()
    s = "abc"
    t = "ab"

    assert sol.isAnagram(s, t) is False


def test_valid_anagram_same_letters_different_counts():
    sol = Solution()
    s = "aacc"
    t = "ccac"

    assert sol.isAnagram(s, t) is False


def test_valid_anagram_with_repeated_characters():
    sol = Solution()
    s = "aaabbb"
    t = "bbbaaa"

    assert sol.isAnagram(s, t) is True


def test_valid_anagram_single_character():
    sol = Solution()
    s = "a"
    t = "a"

    assert sol.isAnagram(s, t) is True


def test_valid_anagram_empty_strings():
    sol = Solution()
    s = ""
    t = ""

    assert sol.isAnagram(s, t) is True
