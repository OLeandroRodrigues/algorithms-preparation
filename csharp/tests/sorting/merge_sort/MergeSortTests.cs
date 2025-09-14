using Algorithms.Sorting;
using Xunit;

namespace Algorithms.Tests.Sorting;

public class MergeSortTests
{
    [Fact]
    public void Sorts_Reverse()
    {
        int[] arr = { 9,8,7,6,5,4,3,2,1 };
        MergeSort.Sort(arr);
        Assert.Equal(new[]{1,2,3,4,5,6,7,8,9}, arr);
    }

    [Fact]
    public void Sorts_AlreadySorted()
    {
        int[] arr = { 1,2,3,4,5,6,7,8,9 };
        MergeSort.Sort(arr);
        Assert.Equal(new[]{1,2,3,4,5,6,7,8,9}, arr);
    }

    [Fact]
    public void Handles_Empty_And_Single()
    {
        int[] empty = Array.Empty<int>();
        MergeSort.Sort(empty);
        Assert.Equal(Array.Empty<int>(), empty);

        int[] one = { 42 };
        MergeSort.Sort(one);
        Assert.Equal(new[]{42}, one);
    }

    [Fact]
    public void Sorts_WithDuplicates()
    {
        int[] arr = { 5, 1, 3, 3, 2, 5, 1 };
        MergeSort.Sort(arr);
        Assert.Equal(new[]{1,1,2,3,3,5,5}, arr);
    }

    [Fact]
    public void Sorts_Negatives()
    {
        int[] arr = { -3, -1, -7, 4, 2, 0 };
        MergeSort.Sort(arr);
        Assert.Equal(new[]{-7, -3, -1, 0, 2, 4}, arr);
    }
}