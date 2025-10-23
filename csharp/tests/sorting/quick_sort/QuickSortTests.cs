using Xunit;
using Algorithms.Sorting;

namespace Algorithms.Tests.Sorting;

public class QuickSortTests
{
    [Fact]
    public void SortsReverse()
    {
        int[] arr = { 9, 8, 7, 6, 5, 4, 3, 2, 1 };
        int[] sorted = QuickSort.Sort(arr);
        Assert.Equal(new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9 }, sorted);
    }

    [Fact]
    public void HandlesEmptyAndSingle()
    {
        int[] empty = { };
        int[] sortedEmpty = QuickSort.Sort(empty);
        Assert.Equal(new int[] { }, sortedEmpty);

        int[] one = { 42 };
        int[] sortedOne = QuickSort.Sort(one);
        Assert.Equal(new int[] { 42 }, sortedOne);
    }

    [Fact]
    public void AlreadySorted()
    {
        int[] arr = { 1, 2, 3, 4 };
        int[] sorted = QuickSort.Sort(arr);
        Assert.Equal(new int[] { 1, 2, 3, 4 }, sorted);
    }

    [Fact]
    public void SortsUnorderedList()
    {
        int[] arr = { 3, 1, 4, 2 };
        int[] sorted = QuickSort.Sort(arr);
        Assert.Equal(new int[] { 1, 2, 3, 4 }, sorted);
    }

    [Fact]
    public void HandlesDuplicates()
    {
        int[] arr = { 4, 2, 2, 3, 1 };
        int[] sorted = QuickSort.Sort(arr);
        Assert.Equal(new int[] { 1, 2, 2, 3, 4 }, sorted);
    }

    [Fact]
    public void HandlesNegativeNumbers()
    {
        int[] arr = { 3, -1, -5, 2, 0 };
        int[] sorted = QuickSort.Sort(arr);
        Assert.Equal(new int[] { -5, -1, 0, 2, 3 }, sorted);
    }

    [Fact]
    public void HandlesAllEqualElements()
    {
        int[] arr = { 7, 7, 7, 7 };
        int[] sorted = QuickSort.Sort(arr);
        Assert.Equal(new int[] { 7, 7, 7, 7 }, sorted);
    }

    [Fact]
    public void SortsLargeList()
    {
        int[] arr = { 10, 3, 7, 2, 9, 1, 5, 8, 6, 4 };
        int[] sorted = QuickSort.Sort(arr);
        Assert.Equal(new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }, sorted);
    }

    [Fact]
    public void HandlesMixedSignsAndDuplicates()
    {
        int[] arr = { 0, -1, 5, -1, 3, 0, 2 };
        int[] sorted = QuickSort.Sort(arr);
        Assert.Equal(new int[] { -1, -1, 0, 0, 2, 3, 5 }, sorted);
    }
}
