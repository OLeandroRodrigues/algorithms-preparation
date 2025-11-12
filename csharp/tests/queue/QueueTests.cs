using System;
using DataStructure.Queue;
using Xunit;

namespace DataStructures.Tests.Queue;

public class QueueTests
{
    [Fact]
    public void Enqueue_Dequeue_ShouldFollowFIFO()
    {
        var q = new DataStructure.Queue.Queue<int>();
        q.Enqueue(1);
        q.Enqueue(2);
        q.Enqueue(3);

        Assert.Equal(1, q.Dequeue());
        Assert.Equal(2, q.Dequeue());
        Assert.Equal(3, q.Dequeue());
        Assert.True(q.IsEmpty());
    }

    [Fact]
    public void Peek_ShouldNotRemoveElement()
    {
        var q = new DataStructure.Queue.Queue<string>();
        q.Enqueue("a");
        q.Enqueue("b");

        Assert.Equal("a", q.Peek());
        Assert.Equal(2, q.Size());

        Assert.Equal("a", q.Dequeue());
        Assert.Equal("b", q.Peek());
        Assert.Equal(1, q.Size());
    }

    [Fact]
    public void IsEmpty_And_Size_WorkAsExpected()
    {
        var q = new DataStructure.Queue.Queue<double>();
        Assert.True(q.IsEmpty());
        Assert.Equal(0, q.Size());

        q.Enqueue(Math.PI);
        Assert.False(q.IsEmpty());
        Assert.Equal(1, q.Size());
    }

    [Fact]
    public void Dequeue_OnEmpty_ShouldThrow()
    {
        var q = new DataStructure.Queue.Queue<int>();
        var ex = Assert.Throws<InvalidOperationException>(() => q.Dequeue());
        Assert.Contains("Dequeue from empty queue", ex.Message);
    }

    [Fact]
    public void Peek_OnEmpty_ShouldThrow()
    {
        var q = new DataStructure.Queue.Queue<int>();
        var ex = Assert.Throws<InvalidOperationException>(() => q.Peek());
        Assert.Contains("Peek from empty queue", ex.Message);
    }
}

