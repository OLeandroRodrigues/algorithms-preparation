using System;
using System.Linq;
using Algorithms.Sorting;
using Xunit;

namespace Algorithms.Tests.Sorting;

public class BucketSortTests
{

    private static bool IsSorted(double[] arr)
    {
        for (int i = 1; i < arr.Length; i++)
            if (arr[i - 1] > arr[i]) return false;
        return true;
    }

    private static bool IsSorted(int[] arr)
    {
        for (int i = 1; i < arr.Length; i++)
            if (arr[i - 1] > arr[i]) return false;
        return true;
    }

    [Fact]
    public void EmptyArray_ReturnsEmpty()
    {
        double[] arr = Array.Empty<double>();
        BucketSort.Sort(arr);
        Assert.Empty(arr);
    }

    [Fact]
    public void SingleElement_ArrayRemainsUnchanged()
    {
        double[] arr = { 0.42 };
        BucketSort.Sort(arr);
        Assert.Single(arr);
        Assert.Equal(0.42, arr[0], 9);
    }

    [Fact]
    public void AlreadySortedArray_RemainsSorted()
    {
        double[] arr = { 0.1, 0.2, 0.3, 0.4 };
        BucketSort.Sort(arr);
        Assert.True(IsSorted(arr));
    }
}
