using Algorithms.Sorting;
using Xunit;

namespace Algorithms.Tests.Sorting;

public class InsertionSortTests
{
    [Fact]
    public void Sorts_Reverse()
    {
        int[] arr = { 9,8,7,6,5,4,3,2,1 };
        InsertionSort.Sort(arr);
        Assert.Equal(new[]{1,2,3,4,5,6,7,8,9}, arr);
    }

    [Fact]
    public void Handles_Empty_And_Single()
    {
        int[] empty = Array.Empty<int>();
        InsertionSort.Sort(empty);
        Assert.Equal(Array.Empty<int>(), empty);

        int[] one = { 42 };
        InsertionSort.Sort(one);
        Assert.Equal(new[]{42}, one);
    }
}