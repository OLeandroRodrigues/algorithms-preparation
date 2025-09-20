using DataStructure.Heap;
using Xunit;

namespace DataStructure.Tests.Heap;

public class MaxHeapTests
{
    [Fact]
    public void Inserts_And_Peeks_Max()
    {
        var heap = new MaxHeap();
        heap.Insert(10);
        heap.Insert(50);
        heap.Insert(30);

        Assert.Equal(50, heap.Peek());
        Assert.Equal(3, heap.Size());
    }

    [Fact]
    public void Pops_In_Descending_Order()
    {
        var heap = new MaxHeap();
        heap.Insert(10);
        heap.Insert(20);
        heap.Insert(5);

        Assert.Equal(20, heap.Pop());
        Assert.Equal(10, heap.Pop());
        Assert.Equal(5, heap.Pop());
        Assert.Equal(0, heap.Size());
    }

    [Fact]
    public void Handles_Empty_Heap()
    {
        var heap = new MaxHeap();

        Assert.Throws<InvalidOperationException>(() => heap.Peek());
        Assert.Throws<InvalidOperationException>(() => heap.Pop());
    }

    [Fact]
    public void Single_Element()
    {
        var heap = new MaxHeap();
        heap.Insert(42);

        Assert.Equal(42, heap.Peek());
        Assert.Equal(42, heap.Pop());
        Assert.Equal(0, heap.Size());
    }

    [Fact]
    public void Mixed_Insert_And_Pop()
    {
        var heap = new MaxHeap();
        heap.Insert(5);
        heap.Insert(15);

        Assert.Equal(15, heap.Pop());

        heap.Insert(20);
        heap.Insert(1);

        Assert.Equal(20, heap.Pop());
        Assert.Equal(5, heap.Pop());
        Assert.Equal(1, heap.Pop());
    }
}