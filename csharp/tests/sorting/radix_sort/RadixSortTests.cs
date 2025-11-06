using System;
using System.Linq;
using Xunit;

using Algorithms.Sorting;
namespace Algorithms.Tests.Sorting;

public class RadixSortTests
{
    private static void AssertSortedEqualsLinqSort(int[] arr)
    {
        var expected = arr.ToArray();
        Array.Sort(expected);
        RadixSort.Sort(arr, verbose: false);
        Assert.Equal(expected, arr);
    }

    [Fact]
    public void Test_Empty()
    {
        var arr = Array.Empty<int>();
        RadixSort.Sort(arr, verbose: false);
        Assert.Empty(arr);
    }

    [Fact]
    public void Test_Single()
    {
        var arr = new[] { 42 };
        RadixSort.Sort(arr, verbose: false);
        Assert.Equal(new[] { 42 }, arr);
    }

    [Fact]
    public void Test_AlreadySorted()
    {
        var arr = new[] { 1, 2, 3, 4, 5, 6 };
        var expected = arr.ToArray();
        RadixSort.Sort(arr, verbose: false);
        Assert.Equal(expected, arr);
    }

    [Fact]
    public void Test_ReverseSorted()
    {
        var arr = new[] { 9, 8, 7, 6, 5, 4, 3, 2, 1 };
        AssertSortedEqualsLinqSort(arr);
    }

    [Fact]
    public void Test_WithDuplicates()
    {
        var arr = new[] { 5, 3, 5, 2, 9, 3, 2, 2, 8, 5 };
        AssertSortedEqualsLinqSort(arr);
    }

    [Fact]
    public void Test_ContainsZero()
    {
        var arr = new[] { 0, 3, 0, 2, 1, 0, 9 };
        AssertSortedEqualsLinqSort(arr);
    }

    [Fact]
    public void Test_RandomSmallReproducible()
    {
        var rng = new Random(1337);
        var arr = Enumerable.Range(0, 2000).Select(_ => rng.Next(0, 10_000)).ToArray();
        AssertSortedEqualsLinqSort(arr);
    }

    [Fact]
    public void Test_RandomMediumReproducible()
    {
        var rng = new Random(2025);
        var arr = Enumerable.Range(0, 20_000).Select(_ => rng.Next(0, 1_000_000)).ToArray();
        AssertSortedEqualsLinqSort(arr);
    }

    [Fact]
    public void Test_LargeDigitsValues()
    {
        var arr = new[] { 1_000_000_007, 1_000_000, 1_000_000_000, 0, 1_000_000_001, 999_999_999 };
        AssertSortedEqualsLinqSort(arr);
    }

    [Fact]
    public void Test_CpfLike_IntRange()
    {
        var rng = new Random(111);
        var arr = Enumerable.Range(0, 3000).Select(_ => rng.Next(0, int.MaxValue)).ToArray();
        AssertSortedEqualsLinqSort(arr);
    }
}
