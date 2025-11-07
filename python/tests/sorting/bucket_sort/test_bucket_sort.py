import random
import math
import pytest

from algorithms.sorting.bucket_sort.bucket_sort import bucket_sort


def is_sorted_non_decreasing(a):
    return all(a[i] <= a[i + 1] for i in range(len(a) - 1))


def test_empty_array_returns_empty():
    assert bucket_sort([]) == []


def test_single_element_array():
    arr = [0.37]
    assert bucket_sort(arr[:]) == arr


def test_already_sorted_array():
    arr = [0.05, 0.10, 0.20, 0.33, 0.40, 0.75, 0.90]
    out = bucket_sort(arr[:])
    assert out == arr
    assert is_sorted_non_decreasing(out)


def test_reversed_array():
    arr = [0.90, 0.80, 0.70, 0.60, 0.50, 0.40, 0.30, 0.20, 0.10]
    out = bucket_sort(arr[:])
    assert out == sorted(arr)
    assert is_sorted_non_decreasing(out)


def test_with_duplicates():
    arr = [0.2, 0.2, 0.5, 0.5, 0.5, 0.1, 0.1]
    out = bucket_sort(arr[:])
    assert out == sorted(arr)
    assert is_sorted_non_decreasing(out)
    from collections import Counter
    assert Counter(out) == Counter(arr)


def test_boundary_value_one_maps_to_last_bucket():
    arr = [0.0, 1.0, 0.5, 0.999999, 0.123456]
    out = bucket_sort(arr[:])
    assert out == sorted(arr)
    assert is_sorted_non_decreasing(out)


def test_random_input_reproducible_sorted():
    rng = random.Random(42)
    arr = [rng.random() for _ in range(200)]
    out = bucket_sort(arr[:])
    assert out == sorted(arr)
    assert is_sorted_non_decreasing(out)


def test_stability_within_same_bucket():
    arr = [0.3000, 0.3000, 0.3000, 0.3000]
    out = bucket_sort(arr[:])
    assert out == arr  # identical and hence same order

def test_precision_edge_values():
    arr = [0.0, 0.1666666, 0.1666667, 0.3333333, 0.3333334, 0.5, 0.6666666, 0.6666667, 0.9999999]
    out = bucket_sort(arr[:])
    assert out == sorted(arr)
    assert is_sorted_non_decreasing(out)


def test_large_input_reasonable_time():
    rng = random.Random(123)
    arr = [rng.random() for _ in range(5000)]
    out = bucket_sort(arr[:])
    assert out == sorted(arr)
