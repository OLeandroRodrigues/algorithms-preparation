using Xunit;
using Algorithms.Sorting.QuickSortRandomized;

namespace Algorithms.Tests.Sorting.QuickSortRandom;

public class QuickSortRandomizedTests
{
    [Fact]
    public void SortsReverseArray()
    {
        int[] arr = { 9, 8, 7, 6, 5, 4, 3, 2, 1 };
        QuickSortRandomized.QuickSort(arr, 0, arr.Length - 1);

        Assert.Equal(new[] { 1, 2, 3, 4, 5, 6, 7, 8, 9 }, arr);
    }

    [Fact]
    public void HandlesEmptyAndSingleElementArrays()
    {
        int[] empty = { };
        QuickSortRandomized.QuickSort(empty, 0, empty.Length - 1);
        Assert.Equal(new int[] { }, empty);

        int[] one = { 42 };
        QuickSortRandomized.QuickSort(one, 0, one.Length - 1);
        Assert.Equal(new[] { 42 }, one);
    }

    [Fact]
    public void KeepsAlreadySortedArray()
    {
        int[] arr = { 1, 2, 3, 4 };
        QuickSortRandomized.QuickSort(arr, 0, arr.Length - 1);

        Assert.Equal(new[] { 1, 2, 3, 4 }, arr);
    }

    [Fact]
    public void SortsUnorderedArray()
    {
        int[] arr = { 3, 1, 4, 2 };
        QuickSortRandomized.QuickSort(arr, 0, arr.Length - 1);

        Assert.Equal(new[] { 1, 2, 3, 4 }, arr);
    }

    [Fact]
    public void HandlesDuplicates()
    {
        int[] arr = { 4, 2, 2, 3, 1 };
        QuickSortRandomized.QuickSort(arr, 0, arr.Length - 1);

        Assert.Equal(new[] { 1, 2, 2, 3, 4 }, arr);
    }

    [Fact]
    public void HandlesNegativeNumbers()
    {
        int[] arr = { 3, -1, -5, 2, 0 };
        QuickSortRandomized.QuickSort(arr, 0, arr.Length - 1);

        Assert.Equal(new[] { -5, -1, 0, 2, 3 }, arr);
    }

    [Fact]
    public void HandlesAllEqualElements()
    {
        int[] arr = { 7, 7, 7, 7 };
        QuickSortRandomized.QuickSort(arr, 0, arr.Length - 1);

        Assert.Equal(new[] { 7, 7, 7, 7 }, arr);
    }

    [Fact]
    public void SortsMixedSignsAndDuplicates()
    {
        int[] arr = { 0, -1, 5, -1, 3, 0, 2 };
        QuickSortRandomized.QuickSort(arr, 0, arr.Length - 1);

        Assert.Equal(new[] { -1, -1, 0, 0, 2, 3, 5 }, arr);
    }

    [Fact]
    public void SortsLargerArray()
    {
        int[] arr = { 10, 3, 7, 2, 9, 1, 5, 8, 6, 4 };
        QuickSortRandomized.QuickSort(arr, 0, arr.Length - 1);

        Assert.Equal(new[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }, arr);
    }
}
