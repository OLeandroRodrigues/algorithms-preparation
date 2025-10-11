using System;
using DataStructure.Generic.Heap;
using Xunit;

namespace DataStructure.Generic.Heap.Tests;

public class MaxHeapGenericTests
{
    [Fact]
    public void Inserts_And_Peeks_Max()
    {
        var heap = new MaxHeap<int>();
        heap.Insert(10);
        heap.Insert(50);
        heap.Insert(30);

        Assert.Equal(50, heap.Peek());
        Assert.Equal(3, heap.Size());
        Assert.False(heap.IsEmpty());
    }

    [Fact]
    public void Pops_In_Descending_Order()
    {
        var heap = new MaxHeap<int>();
        heap.Insert(10);
        heap.Insert(20);
        heap.Insert(5);
        heap.Insert(40);

        Assert.Equal(40, heap.Pop());
        Assert.Equal(20, heap.Pop());
        Assert.Equal(10, heap.Pop());
        Assert.Equal(5, heap.Pop());
        Assert.True(heap.IsEmpty());
        Assert.Equal(0, heap.Size());
    }

    [Fact]
    public void Peek_And_Pop_On_Empty_Throw()
    {
        var heap = new MaxHeap<int>();
        Assert.Throws<InvalidOperationException>(() => heap.Peek());
        Assert.Throws<InvalidOperationException>(() => heap.Pop());
    }

    [Fact]
    public void Single_Element_Behavior()
    {
        var heap = new MaxHeap<int>();
        heap.Insert(42);

        Assert.Equal(42, heap.Peek());
        Assert.Equal(42, heap.Pop());
        Assert.True(heap.IsEmpty());
        Assert.Equal(0, heap.Size());
    }

    [Fact]
    public void Mixed_Insert_And_Pop_Sequence()
    {
        var heap = new MaxHeap<int>();
        heap.Insert(5);
        heap.Insert(15);
        Assert.Equal(15, heap.Pop());

        heap.Insert(20);
        heap.Insert(1);
        Assert.Equal(20, heap.Pop());
        Assert.Equal(5, heap.Pop());
        Assert.Equal(1, heap.Pop());
        Assert.True(heap.IsEmpty());
    }

    [Fact]
    public void Works_With_Strings()
    {
        var heap = new MaxHeap<string>();
        heap.Insert("apple");
        heap.Insert("banana");
        heap.Insert("pear");

        Assert.Equal("pear", heap.Peek());
        Assert.Equal("pear", heap.Pop());
        Assert.Equal("banana", heap.Pop());
        Assert.Equal("apple", heap.Pop());
        Assert.True(heap.IsEmpty());
    }

    [Fact]
    public void Works_With_Custom_Comparable_Type()
    {
        var heap = new MaxHeap<Job>();
        heap.Insert(new Job("low", 1));
        heap.Insert(new Job("mid", 5));
        heap.Insert(new Job("high", 10));
        heap.Insert(new Job("same1", 10));
        heap.Insert(new Job("same2", 10));

        Assert.Equal(10, heap.Pop().Priority);
        Assert.Equal(10, heap.Pop().Priority);
        Assert.Equal(10, heap.Pop().Priority);
        Assert.Equal(5, heap.Pop().Priority);
        Assert.Equal(1, heap.Pop().Priority);
        Assert.True(heap.IsEmpty());
    }

    [Fact]
    public void Stress_Insert_And_Pop_Many()
    {
        var heap = new MaxHeap<int>();
        for (int i = 0; i < 200; i++)
            heap.Insert(i);

        for (int expected = 199; expected >= 0; expected--)
            Assert.Equal(expected, heap.Pop());

        Assert.True(heap.IsEmpty());
    }

    private sealed class Job : IComparable<Job>
    {
        public string Id { get; }
        public int Priority { get; }

        public Job(string id, int priority)
        {
            Id = id;
            Priority = priority;
        }

        public int CompareTo(Job? other)
        {
            if (other is null) return 1;
            return Priority.CompareTo(other.Priority); 
        }

        public override string ToString() => $"{Id}({Priority})";
    }
}
