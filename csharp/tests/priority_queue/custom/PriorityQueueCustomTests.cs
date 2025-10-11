using System;
using DataStructure.PriorityQueue.Custom;
using Xunit;

namespace DataStructure.PriorityQueue.Custom.Tests;

public class PriorityQueueCustomTests
{
    [Fact]
    public void MaxPriority_ComesOutFirst()
    {
        var pq = new PriorityQueueCustom<string>();
        pq.Push("low", 1);
        pq.Push("mid", 5);
        pq.Push("high", 10);

        Assert.Equal(3, pq.Size());
        Assert.Equal("high", pq.Peek());
        Assert.Equal("high", pq.Pop());
        Assert.Equal("mid", pq.Pop());
        Assert.Equal("low", pq.Pop());
        Assert.True(pq.IsEmpty());
    }

    [Fact]
    public void Stability_FIFO_WhenPriorityIsEqual()
    {
        var pq = new PriorityQueueCustom<string>();
        pq.Push("A", 10); 
        pq.Push("B", 10); 
        pq.Push("C", 10); 

        Assert.Equal("A", pq.Pop());
        Assert.Equal("B", pq.Pop());
        Assert.Equal("C", pq.Pop());
        Assert.True(pq.IsEmpty());
    }

    [Fact]
    public void Peek_DoesNotRemove()
    {
        var pq = new PriorityQueueCustom<string>();
        pq.Push("x", 2);
        pq.Push("y", 7);
        pq.Push("z", 5);

        Assert.Equal(3, pq.Size());
        Assert.Equal("y", pq.Peek()); 
        Assert.Equal(3, pq.Size());  
        Assert.Equal("y", pq.Pop());
        Assert.Equal("z", pq.Pop());
        Assert.Equal("x", pq.Pop());
    }

    [Fact]
    public void Size_And_IsEmpty_AreConsistent()
    {
        var pq = new PriorityQueueCustom<int>();
        Assert.True(pq.IsEmpty());
        Assert.Equal(0, pq.Size());

        pq.Push(1, 1);
        pq.Push(2, 2);

        Assert.False(pq.IsEmpty());
        Assert.Equal(2, pq.Size());

        _ = pq.Pop();
        Assert.Equal(1, pq.Size());

        _ = pq.Pop();
        Assert.True(pq.IsEmpty());
        Assert.Equal(0, pq.Size());
    }

    [Fact]
    public void Pop_OnEmpty_Throws()
    {
        var pq = new PriorityQueueCustom<int>();
        Assert.Throws<InvalidOperationException>(() => pq.Pop());
    }

    [Fact]
    public void Peek_OnEmpty_Throws()
    {
        var pq = new PriorityQueueCustom<int>();
        Assert.Throws<InvalidOperationException>(() => pq.Peek());
    }

    [Fact]
    public void Works_With_Custom_Object_Type()
    {
        var pq = new PriorityQueueCustom<Job>();
        pq.Push(new Job("J1", "alpha"), 3);
        pq.Push(new Job("J2", "beta"), 10);
        pq.Push(new Job("J3", "gamma"), 10);

        Assert.Equal("J2", pq.Pop().Id);
        Assert.Equal("J3", pq.Pop().Id);
        Assert.Equal("J1", pq.Pop().Id);
        Assert.True(pq.IsEmpty());
    }

    [Fact]
    public void Mixed_Priorities_And_Ties()
    {
        var pq = new PriorityQueueCustom<string>();
        pq.Push("A1", 10);
        pq.Push("B",   5);
        pq.Push("A2", 10);
        pq.Push("C",   7);
        pq.Push("A3", 10);

        Assert.Equal("A1", pq.Pop());
        Assert.Equal("A2", pq.Pop());
        Assert.Equal("A3", pq.Pop());
        Assert.Equal("C",  pq.Pop());
        Assert.Equal("B",  pq.Pop());
        Assert.True(pq.IsEmpty());
    }

    private sealed class Job
    {
        public string Id { get; }
        public string Payload { get; }
        public Job(string id, string payload)
        {
            Id = id;
            Payload = payload;
        }
    }
}
