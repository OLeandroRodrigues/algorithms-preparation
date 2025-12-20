import pytest
from problems.boyer_moore.string_search.find_word_in_text import Solution


def test_find_word_basic_match():
    sol = Solution()
    text = "here is a simple example"
    pattern = "simple"
    assert sol.findWord(text, pattern) == 10


def test_find_word_match_at_start():
    sol = Solution()
    text = "abcde"
    pattern = "abc"
    assert sol.findWord(text, pattern) == 0


def test_find_word_match_at_end():
    sol = Solution()
    text = "abcde"
    pattern = "cde"
    assert sol.findWord(text, pattern) == 2


def test_find_word_no_match():
    sol = Solution()
    text = "aaaaa"
    pattern = "bba"
    assert sol.findWord(text, pattern) == -1


def test_find_word_empty_pattern_returns_zero():
    sol = Solution()
    text = "abc"
    pattern = ""
    assert sol.findWord(text, pattern) == 0


def test_find_word_pattern_longer_than_text():
    sol = Solution()
    text = "ab"
    pattern = "abc"
    assert sol.findWord(text, pattern) == -1


def test_find_word_repeated_characters():
    sol = Solution()
    text = "aaaaaa"
    pattern = "aaa"
    assert sol.findWord(text, pattern) == 0


def test_find_word_overlapping_occurrences_first_index():
    sol = Solution()
    text = "abababab"
    pattern = "abab"
    assert sol.findWord(text, pattern) == 0


def test_find_word_single_character_present():
    sol = Solution()
    text = "xyz"
    pattern = "y"
    assert sol.findWord(text, pattern) == 1


def test_find_word_single_character_absent():
    sol = Solution()
    text = "xyz"
    pattern = "a"
    assert sol.findWord(text, pattern) == -1


def test_find_word_case_sensitive():
    sol = Solution()
    text = "AbcABC"
    pattern = "ABC"
    assert sol.findWord(text, pattern) == 3


def test_build_bad_character_table_last_occurrence():
    sol = Solution()
    pattern = "abac"
    table = sol._build_bad_character_table(pattern)
    assert table["a"] == 2
    assert table["b"] == 1
    assert table["c"] == 3
    assert table.get("z", -1) == -1


def test_build_good_suffix_table_length():
    sol = Solution()
    pattern = "example"
    shift = sol._build_good_suffix_table(pattern)
    assert isinstance(shift, list)
    assert len(shift) == len(pattern) + 1
    # shifts should be positive integers
    assert all(isinstance(x, int) and x > 0 for x in shift)
