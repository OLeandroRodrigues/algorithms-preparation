using DataStructure.Heap;
using Xunit;

namespace DataStructure.Tests.Heap;

public class MinHeapTests
{
    [Fact]
    public void Inserts_And_Peeks_Min()
    {
        var heap = new MinHeap();
        heap.Insert(10);
        heap.Insert(50);
        heap.Insert(5);

        Assert.Equal(5, heap.Peek());
        Assert.Equal(3, heap.Size());
    }

    [Fact]
    public void Pops_In_Ascending_Order()
    {
        var heap = new MinHeap();
        heap.Insert(10);
        heap.Insert(20);
        heap.Insert(5);

        Assert.Equal(5, heap.Pop());
        Assert.Equal(10, heap.Pop());
        Assert.Equal(20, heap.Pop());
        Assert.Equal(0, heap.Size());
    }

    [Fact]
    public void Handles_Empty_Heap()
    {
        var heap = new MinHeap();

        Assert.Throws<InvalidOperationException>(() => heap.Peek());
        Assert.Throws<InvalidOperationException>(() => heap.Pop());
    }

    [Fact]
    public void Single_Element()
    {
        var heap = new MinHeap();
        heap.Insert(42);

        Assert.Equal(42, heap.Peek());
        Assert.Equal(42, heap.Pop());
        Assert.Equal(0, heap.Size());
    }

    [Fact]
    public void Mixed_Insert_And_Pop()
    {
        var heap = new MinHeap();
        heap.Insert(30);
        heap.Insert(10);
        heap.Insert(20);

        Assert.Equal(10, heap.Pop());

        heap.Insert(5);
        heap.Insert(40);

        Assert.Equal(5, heap.Pop());
        Assert.Equal(20, heap.Pop());
        Assert.Equal(30, heap.Pop());
        Assert.Equal(40, heap.Pop());
    }
}