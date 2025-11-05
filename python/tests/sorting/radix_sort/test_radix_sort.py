

import random
import sys


from algorithms.sorting.radix_sort import radix_sort

def test_empty_list():
    arr = []
    radix_sort(arr)
    assert arr == []


def test_single_element():
    arr = [42]
    radix_sort(arr)
    assert arr == [42]


def test_all_equal_elements():
    arr = [7, 7, 7, 7, 7]
    expected = sorted(arr)
    radix_sort(arr)
    assert arr == expected


def test_contains_zero():
    arr = [0, 3, 0, 2, 1, 0, 9]
    expected = sorted(arr)
    radix_sort(arr)
    assert arr == expected


def test_already_sorted():
    arr = [1, 2, 3, 4, 5, 6]
    expected = arr[:]
    radix_sort(arr)
    assert arr == expected


def test_reverse_sorted():
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected = sorted(arr)
    radix_sort(arr)
    assert arr == expected


def test_with_duplicates():
    arr = [5, 3, 5, 2, 9, 3, 2, 2, 8, 5]
    expected = sorted(arr)
    radix_sort(arr)
    assert arr == expected


def test_random_small_reproducible():
    rng = random.Random(1337)
    arr = [rng.randrange(0, 10_000) for _ in range(2000)]
    expected = sorted(arr)
    radix_sort(arr)
    assert arr == expected


def test_random_medium_reproducible():
    rng = random.Random(2025)
    arr = [rng.randrange(0, 1_000_000) for _ in range(20_000)]
    expected = sorted(arr)
    radix_sort(arr)
    assert arr == expected


def test_large_digits_values():
    # numbers with many digits (still non-negative)
    arr = [10**9 + 7, 10**6, 10**12, 0, 10**12 + 1, 999_999_999]
    expected = sorted(arr)
    radix_sort(arr)
    assert arr == expected


def test_cpf_like_values():
    rng = random.Random(111)
    arr = [rng.randrange(0, 100_000_000_000) for _ in range(3000)]
    expected = sorted(arr)
    radix_sort(arr)
    assert arr == expected


def test_stress_small_if_fast():
    
    rng = random.Random(7)
    arr = [rng.randrange(0, 1_000_000) for _ in range(50_000)]
    expected = sorted(arr)
    radix_sort(arr)
    assert arr == expected


def test_does_not_support_negative_numbers_by_design():
    
    arr = [3, -1, 2]
    assert any(x < 0 for x in arr), "fixture invalid: it must contain negative"
    