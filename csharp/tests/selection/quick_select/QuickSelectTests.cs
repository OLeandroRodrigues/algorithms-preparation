using System;
using Xunit;
using Selection;

namespace Algorithms.Selection.Tests;

public class QuickSelectTests
{
    [Fact]
    public void FindsKthSmallestBasic()
    {
        int[] arr = { 7, 10, 4, 3, 20, 15 };
        int result = QuickSelect.QuickSelectAlgorithm(arr, 0, arr.Length - 1, 3);
        Assert.Equal(7, result); // 3rd smallest
    }

    [Fact]
    public void FindsMinimumAndMaximum()
    {
        int[] arr = { 8, 3, 5, 12, 1, 9 };
        int min = QuickSelect.QuickSelectAlgorithm(arr, 0, arr.Length - 1, 1);
        int max = QuickSelect.QuickSelectAlgorithm(arr, 0, arr.Length - 1, arr.Length);
        Assert.Equal(1, min);
        Assert.Equal(12, max);
    }

    [Fact]
    public void HandlesDuplicates()
    {
        int[] arr = { 4, 2, 2, 3, 1 };
        int result = QuickSelect.QuickSelectAlgorithm(arr, 0, arr.Length - 1, 3);
        Assert.Equal(2, result);
    }

    [Fact]
    public void HandlesNegativeNumbers()
    {
        int[] arr = { 3, -1, -5, 2, 0 };
        int result = QuickSelect.QuickSelectAlgorithm(arr, 0, arr.Length - 1, 2);
        Assert.Equal(-1, result);
    }

    [Fact]
    public void HandlesAllEqualElements()
    {
        int[] arr = { 7, 7, 7, 7 };
        int result = QuickSelect.QuickSelectAlgorithm(arr, 0, arr.Length - 1, 2);
        Assert.Equal(7, result);
    }

    [Fact]
    public void ThrowsIfKOutOfRange()
    {
        int[] arr = { 1, 2, 3, 4, 5 };
        Assert.Throws<IndexOutOfRangeException>(() =>
            QuickSelect.QuickSelectAlgorithm(arr, 0, arr.Length - 1, 0));
        Assert.Throws<IndexOutOfRangeException>(() =>
            QuickSelect.QuickSelectAlgorithm(arr, 0, arr.Length - 1, 6));
    }

    [Fact]
    public void SingleElementArray()
    {
        int[] arr = { 42 };
        int result = QuickSelect.QuickSelectAlgorithm(arr, 0, 0, 1);
        Assert.Equal(42, result);
    }

    [Fact]
    public void WorksWithReverseOrderedArray()
    {
        int[] arr = { 9, 8, 7, 6, 5 };
        int result = QuickSelect.QuickSelectAlgorithm(arr, 0, arr.Length - 1, 2);
        Assert.Equal(6, result);
    }

    [Fact]
    public void WorksWithAlreadySortedArray()
    {
        int[] arr = { 1, 2, 3, 4, 5 };
        int result = QuickSelect.QuickSelectAlgorithm(arr, 0, arr.Length - 1, 4);
        Assert.Equal(4, result);
    }

    [Fact]
    public void HandlesLargeList()
    {
        int[] arr = { 10, 3, 7, 2, 9, 1, 5, 8, 6, 4 };
        int result = QuickSelect.QuickSelectAlgorithm(arr, 0, arr.Length - 1, 5);
        Assert.Equal(5, result);
    }
}
