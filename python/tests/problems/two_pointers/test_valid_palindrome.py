import pytest
from problems.two_pointers.valid_palindrome import Solution


def test_example_true():
    sol = Solution()
    assert sol.isPalindrome("A man, a plan, a canal: Panama") is True


def test_example_false():
    sol = Solution()
    assert sol.isPalindrome("race a car") is False


def test_empty_string():
    sol = Solution()
    assert sol.isPalindrome("") is True


def test_only_spaces():
    sol = Solution()
    assert sol.isPalindrome("   ") is True


def test_only_symbols():
    sol = Solution()
    assert sol.isPalindrome("!!!") is True


def test_simple_palindrome():
    sol = Solution()
    assert sol.isPalindrome("abba") is True


def test_case_insensitive():
    sol = Solution()
    assert sol.isPalindrome("Aa") is True


def test_numbers_false():
    sol = Solution()
    assert sol.isPalindrome("0P") is False


def test_mixed_true():
    sol = Solution()
    assert sol.isPalindrome("1a2a1") is True


def test_mixed_false():
    sol = Solution()
    assert sol.isPalindrome("1a2") is False