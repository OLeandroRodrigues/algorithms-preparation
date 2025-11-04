using Xunit;
using Algorithms.Sorting;

namespace Algorithms.Tests.Sorting;

public class CountingSortTests
{
    [Fact]
    public void BasicUnsortedArray()
    {
        int[] arr = { 4, 2, 2, 8, 3, 3, 1 };
        int[] expected = { 1, 2, 2, 3, 3, 4, 8 };
        Assert.Equal(expected, CountingSort.Sort(arr));
    }

    [Fact]
    public void EmptyArrayReturnsEmpty()
    {
        int[] arr = { };
        int[] expected = { };
        Assert.Equal(expected, CountingSort.Sort(arr));
    }

    [Fact]
    public void AlreadySortedArrayRemainsTheSame()
    {
        int[] arr = { 1, 2, 3, 4, 5 };
        int[] expected = { 1, 2, 3, 4, 5 };
        Assert.Equal(expected, CountingSort.Sort(arr));
    }

    [Fact]
    public void ReverseSortedArrayGetsSorted()
    {
        int[] arr = { 5, 4, 3, 2, 1 };
        int[] expected = { 1, 2, 3, 4, 5 };
        Assert.Equal(expected, CountingSort.Sort(arr));
    }

    [Fact]
    public void ArrayWithDuplicates()
    {
        int[] arr = { 5, 5, 5, 2, 2, 9, 9, 1 };
        int[] expected = { 1, 2, 2, 5, 5, 5, 9, 9 };
        Assert.Equal(expected, CountingSort.Sort(arr));
    }

    [Fact]
    public void ArrayAllEqualValues()
    {
        int[] arr = { 7, 7, 7, 7 };
        int[] expected = { 7, 7, 7, 7 };
        Assert.Equal(expected, CountingSort.Sort(arr));
    }

    [Fact]
    public void ArrayWithZeroIncluded()
    {
        int[] arr = { 0, 5, 0, 3, 2, 2 };
        int[] expected = { 0, 0, 2, 2, 3, 5 };
        Assert.Equal(expected, CountingSort.Sort(arr));
    }

    [Fact]
    public void LargeValuesWithinRange()
    {
        int[] arr = { 100, 1, 50, 50, 100, 0 };
        int[] expected = { 0, 1, 50, 50, 100, 100 };
        Assert.Equal(expected, CountingSort.Sort(arr));
    }

    [Fact]
    public void SingleElementArray()
    {
        int[] arr = { 42 };
        int[] expected = { 42 };
        Assert.Equal(expected, CountingSort.Sort(arr));
    }

    [Fact]
    public void InputArrayIsNotModified()
    {
        int[] arr = { 4, 1, 4, 3 };
        int[] copy = (int[])arr.Clone();
        _ = CountingSort.Sort(arr);
        // Ensure the original input is not modified (function should be pure)
        Assert.Equal(copy, arr);
    }
}

