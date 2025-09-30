using System;
using Xunit;
using Algorithms.Sorting;

namespace Algorithms.Tests.Sorting;

public class HeapSortInPlaceTests
{
    [Fact]
    public void Sort_Basic()
    {
        var arr = new[] { 7, 51, 4, 10, 15, 30, 50 };
        var expected = new[] { 4, 7, 10, 15, 30, 50, 51 };

        HeapSortInPlace.HeapSort(arr);

        Assert.Equal(expected, arr);
    }

    [Fact]
    public void Sort_EmptyArray()
    {
        var arr = Array.Empty<int>();
        var expected = Array.Empty<int>();

        HeapSortInPlace.HeapSort(arr);

        Assert.Equal(expected, arr);
    }

    [Fact]
    public void Sort_SingleElement()
    {
        var arr = new[] { 42 };
        var expected = new[] { 42 };

        HeapSortInPlace.HeapSort(arr);

        Assert.Equal(expected, arr);
    }

    [Fact]
    public void Sort_AllEqual()
    {
        var arr = new[] { 7, 7, 7, 7, 7 };
        var expected = new[] { 7, 7, 7, 7, 7 };

        HeapSortInPlace.HeapSort(arr);

        Assert.Equal(expected, arr);
    }

    [Fact]
    public void Sort_AlreadySorted()
    {
        var arr = new[] { 1, 2, 3, 4, 5, 6 };
        var expected = new[] { 1, 2, 3, 4, 5, 6 };

        HeapSortInPlace.HeapSort(arr);

        Assert.Equal(expected, arr);
    }

    [Fact]
    public void Sort_ReverseSorted()
    {
        var arr = new[] { 9, 8, 7, 6, 5, 4, 3 };
        var expected = new[] { 3, 4, 5, 6, 7, 8, 9 };

        HeapSortInPlace.HeapSort(arr);

        Assert.Equal(expected, arr);
    }

    [Fact]
    public void Sort_WithDuplicates()
    {
        var arr = new[] { 4, 5, 5, 10, 10, 8, 2, 100, 50, 30, 1 };
        var expected = new[] { 1, 2, 4, 5, 5, 8, 10, 10, 30, 50, 100 };

        HeapSortInPlace.HeapSort(arr);

        Assert.Equal(expected, arr);
    }

    [Fact]
    public void Sort_NegativesAndPositives()
    {
        var arr = new[] { 0, -5, 3, -1, 2, -5, 8 };
        var expected = new[] { -5, -5, -1, 0, 2, 3, 8 };

        HeapSortInPlace.HeapSort(arr);

        Assert.Equal(expected, arr);
    }
}

