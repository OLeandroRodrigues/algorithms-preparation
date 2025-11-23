using Xunit;
using DataStructures.LinkedList.CircularLinkedList;

namespace DataStructures.Tests.LinkedList.CircularLinkedList;

public class CircularLinkedListTests
{
    [Fact]
    public void NewList_ShouldBeEmpty()
    {
        var cll = new CircularLinkedList<int>();

        Assert.True(cll.IsEmpty());
        Assert.Equal(0, cll.Size);
        Assert.Equal("CircularLinkedList([])", cll.ToString());
    }

    [Fact]
    public void AddFirst_SingleElement()
    {
        var cll = new CircularLinkedList<int>();
        cll.AddFirst(10);

        Assert.False(cll.IsEmpty());
        Assert.Equal(1, cll.Size);
        Assert.Equal(10, cll.GetFirst());
        Assert.Equal(10, cll.GetLast());

        // circular property: tail.next == tail
        Assert.NotNull(cll.Tail);
        Assert.Same(cll.Tail, cll.Tail.Next);
    }

    [Fact]
    public void AddFirst_MultipleElements()
    {
        var cll = new CircularLinkedList<int>();

        cll.AddFirst(10);
        cll.AddFirst(20);
        cll.AddFirst(30);

        Assert.Equal(3, cll.Size);
        Assert.Equal(30, cll.GetFirst());
        Assert.Equal(10, cll.GetLast());

        Assert.Equal("CircularLinkedList([30, 20, 10])", cll.ToString());
    }

    [Fact]
    public void AddLast_ShouldPreserveOrder()
    {
        var cll = new CircularLinkedList<int>();

        cll.AddLast(10);
        cll.AddLast(20);
        cll.AddLast(30);

        Assert.Equal(3, cll.Size);
        Assert.Equal(10, cll.GetFirst());
        Assert.Equal(30, cll.GetLast());
        Assert.Equal("CircularLinkedList([10, 20, 30])", cll.ToString());
    }

    [Fact]
    public void RemoveFirst_SingleElement()
    {
        var cll = new CircularLinkedList<int>();
        cll.AddLast(42);

        int removed = cll.RemoveFirst();
        Assert.Equal(42, removed);

        Assert.True(cll.IsEmpty());
        Assert.Equal(0, cll.Size);
        Assert.Null(cll.Tail);
    }

    [Fact]
    public void RemoveFirst_MultipleElements()
    {
        var cll = new CircularLinkedList<int>();

        cll.AddLast(10);
        cll.AddLast(20);
        cll.AddLast(30);

        Assert.Equal(3, cll.Size);

        Assert.Equal(10, cll.RemoveFirst());  // remove head
        Assert.Equal(2, cll.Size);
        Assert.Equal(20, cll.GetFirst());
        Assert.Equal(30, cll.GetLast());

        Assert.Equal(20, cll.RemoveFirst());
        Assert.Equal(1, cll.Size);
        Assert.Equal(30, cll.GetFirst());
        Assert.Equal(30, cll.GetLast());

        Assert.Equal(30, cll.RemoveFirst());
        Assert.True(cll.IsEmpty());
        Assert.Equal(0, cll.Size);
    }

    [Fact]
    public void RemoveFirst_FromEmpty_ShouldThrow()
    {
        var cll = new CircularLinkedList<int>();

        Assert.Throws<InvalidOperationException>(() => cll.RemoveFirst());
    }

    [Fact]
    public void GetFirst_And_GetLast_FromEmpty_ShouldThrow()
    {
        var cll = new CircularLinkedList<int>();

        Assert.Throws<InvalidOperationException>(() => cll.GetFirst());
        Assert.Throws<InvalidOperationException>(() => cll.GetLast());
    }

    [Fact]
    public void Find_ExistingElements()
    {
        var cll = new CircularLinkedList<string>();

        cll.AddLast("a");
        cll.AddLast("b");
        cll.AddLast("c");

        var nodeB = cll.Find("b");
        Assert.NotNull(nodeB);
        Assert.Equal("b", nodeB.Value);

        var nodeC = cll.Find("c");
        Assert.NotNull(nodeC);
        Assert.Equal("c", nodeC.Value);
    }

    [Fact]
    public void Find_NonExistingElement_ShouldReturnNull()
    {
        var cll = new CircularLinkedList<int>();

        cll.AddLast(1);
        cll.AddLast(2);
        cll.AddLast(3);

        var node = cll.Find(99);
        Assert.Null(node);
    }

    [Fact]
    public void CircularTraversal_ShouldVisitAllOnce()
    {
        var cll = new CircularLinkedList<int>();

        cll.AddLast(10);
        cll.AddLast(20);
        cll.AddLast(30);

        var head = cll.Tail.Next;
        var current = head;

        int[] values = new int[cll.Size];
        int i = 0;

        do
        {
            values[i++] = current.Value;
            current = current.Next;
        }
        while (current != head);

        Assert.Equal(new[] { 10, 20, 30 }, values);
    }
}

