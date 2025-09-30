using Algorithms.Sorting;
using System;
using System.Collections.Generic;
using Xunit;

namespace Algorithms.Tests.Sorting;

public class HeapSortTest
{
    [Fact]
    public void TestSortAscBasic()
    {
        var input = new List<int> { 4, 5, 5, 10, 10, 8, 2, 100, 50, 30, 1 };
        var expected = new List<int> { 1, 2, 4, 5, 5, 8, 10, 10, 30, 50, 100 };

        var result = HeapSort.SortAsc(input);

        Assert.Equal(expected, result);
    }

    [Fact]
    public void TestSortDescBasic()
    {
        var input = new List<int> { 4, 5, 5, 10, 10, 8, 2, 100, 50, 30, 1 };
        var expected = new List<int> { 100, 50, 30, 10, 10, 8, 5, 5, 4, 2, 1 };

        var result = HeapSort.SortDesc(input);

        Assert.Equal(expected, result);
    }

    [Fact]
    public void TestEmptyList()
    {
        var input = new List<int>();
        var expected = new List<int>();

        Assert.Equal(expected, HeapSort.SortAsc(input));
        Assert.Equal(expected, HeapSort.SortDesc(input));
    }

    [Fact]
    public void TestSingleElementList()
    {
        var input = new List<int> { 42 };
        var expectedAsc = new List<int> { 42 };
        var expectedDesc = new List<int> { 42 };

        Assert.Equal(expectedAsc, HeapSort.SortAsc(input));
        Assert.Equal(expectedDesc, HeapSort.SortDesc(input));
    }

    [Fact]
    public void TestAllEqualElements()
    {
        var input = new List<int> { 7, 7, 7, 7, 7 };
        var expected = new List<int> { 7, 7, 7, 7, 7 };

        Assert.Equal(expected, HeapSort.SortAsc(input));
        Assert.Equal(expected, HeapSort.SortDesc(input));
    }
}
