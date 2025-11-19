using System;
using System.Collections.Generic;
using DataStructures.LinkedList;
using Xunit;

namespace DataStructures.LinkedList.Tests;

public class DoublyLinkedListTests
{
    // Helpers ----------------------------------------------

    private static List<T> ToList<T>(DoublyLinkedList<T> list)
    {
        var result = new List<T>();
        foreach (var item in list)
            result.Add(item);
        return result;
    }

    private static List<T> ToReversedList<T>(DoublyLinkedList<T> list)
    {
        var result = new List<T>();
        foreach (var item in list.AsReversed())
            result.Add(item);
        return result;
    }

    // Initial state ----------------------------------------

    [Fact]
    public void NewList_ShouldBeEmpty()
    {
        var list = new DoublyLinkedList<int>();

        Assert.True(list.IsEmpty);
        Assert.Equal(0, list.Count);
        Assert.Equal("DoublyLinkedList[]", list.ToString());
        Assert.Empty(ToList(list));

        Assert.Throws<InvalidOperationException>(() => list.PeekFirst());
        Assert.Throws<InvalidOperationException>(() => list.PeekLast());
    }

    [Fact]
    public void Constructor_WithSource_PopulatesList()
    {
        var list = new DoublyLinkedList<int>(new[] { 1, 2, 3 });

        Assert.False(list.IsEmpty);
        Assert.Equal(3, list.Count);
        Assert.Equal(new List<int> { 1, 2, 3 }, ToList(list));
    }

    // AddFirst / AddLast -----------------------------------

    [Fact]
    public void AddFirst_OnEmptyList_SetsFirstElement()
    {
        var list = new DoublyLinkedList<int>();

        list.AddFirst(10);

        Assert.Equal(1, list.Count);
        Assert.Equal(new List<int> { 10 }, ToList(list));
        Assert.Equal(10, list.PeekFirst());
        Assert.Equal(10, list.PeekLast());
    }

    [Fact]
    public void AddFirst_OnNonEmptyList_AddsAtFront()
    {
        var list = new DoublyLinkedList<int>();

        list.AddFirst(10);
        list.AddFirst(20);

        Assert.Equal(new List<int> { 20, 10 }, ToList(list));
    }

    [Fact]
    public void AddLast_OnEmptyList_SetsFirstElement()
    {
        var list = new DoublyLinkedList<int>();

        list.AddLast(10);

        Assert.Equal(1, list.Count);
        Assert.Equal(new List<int> { 10 }, ToList(list));
        Assert.Equal(10, list.PeekFirst());
        Assert.Equal(10, list.PeekLast());
    }

    [Fact]
    public void AddLast_OnNonEmptyList_AppendsToEnd()
    {
        var list = new DoublyLinkedList<int>();

        list.AddLast(10);
        list.AddLast(20);

        Assert.Equal(new List<int> { 10, 20 }, ToList(list));
    }

    // Peek -------------------------------------------------

    [Fact]
    public void Peek_OnEmpty_Throws()
    {
        var list = new DoublyLinkedList<int>();

        Assert.Throws<InvalidOperationException>(() => list.PeekFirst());
        Assert.Throws<InvalidOperationException>(() => list.PeekLast());
    }

    [Fact]
    public void Peek_OnNonEmpty_ReturnsValues()
    {
        var list = new DoublyLinkedList<int>();

        list.AddLast(10);
        list.AddLast(20);

        Assert.Equal(10, list.PeekFirst());
        Assert.Equal(20, list.PeekLast());
    }

    // RemoveFirst / RemoveLast -----------------------------

    [Fact]
    public void RemoveFirst_SingleElement_ClearsList()
    {
        var list = new DoublyLinkedList<int>();
        list.AddLast(10);

        var value = list.RemoveFirst();

        Assert.Equal(10, value);
        Assert.True(list.IsEmpty);
        Assert.Empty(ToList(list));
        Assert.Throws<InvalidOperationException>(() => list.PeekFirst());
        Assert.Throws<InvalidOperationException>(() => list.PeekLast());
    }

    [Fact]
    public void RemoveFirst_MultipleElements_RemovesFront()
    {
        var list = new DoublyLinkedList<int>();
        list.AddLast(10);
        list.AddLast(20);
        list.AddLast(30);

        var value = list.RemoveFirst();

        Assert.Equal(10, value);
        Assert.Equal(new List<int> { 20, 30 }, ToList(list));
        Assert.Equal(20, list.PeekFirst());
    }

    [Fact]
    public void RemoveFirst_OnEmpty_Throws()
    {
        var list = new DoublyLinkedList<int>();

        Assert.Throws<InvalidOperationException>(() => list.RemoveFirst());
    }

    [Fact]
    public void RemoveLast_SingleElement_ClearsList()
    {
        var list = new DoublyLinkedList<int>();
        list.AddLast(10);

        var value = list.RemoveLast();

        Assert.Equal(10, value);
        Assert.True(list.IsEmpty);
        Assert.Empty(ToList(list));
        Assert.Throws<InvalidOperationException>(() => list.PeekFirst());
        Assert.Throws<InvalidOperationException>(() => list.PeekLast());
    }

    [Fact]
    public void RemoveLast_MultipleElements_RemovesTail()
    {
        var list = new DoublyLinkedList<int>();
        list.AddLast(10);
        list.AddLast(20);
        list.AddLast(30);

        var value = list.RemoveLast();

        Assert.Equal(30, value);
        Assert.Equal(new List<int> { 10, 20 }, ToList(list));
        Assert.Equal(20, list.PeekLast());
    }

    [Fact]
    public void RemoveLast_OnEmpty_Throws()
    {
        var list = new DoublyLinkedList<int>();

        Assert.Throws<InvalidOperationException>(() => list.RemoveLast());
    }

    // Contains / RemoveFirstOccurrence ---------------------

    [Fact]
    public void Contains_WorksCorrectly()
    {
        var list = new DoublyLinkedList<int>(new[] { 1, 2, 3 });

        Assert.True(list.Contains(1));
        Assert.True(list.Contains(2));
        Assert.True(list.Contains(3));
        Assert.False(list.Contains(99));
    }

    [Fact]
    public void RemoveFirstOccurrence_RemovesExistingValue()
    {
        var list = new DoublyLinkedList<int>(new[] { 1, 2, 3 });

        var removed = list.RemoveFirstOccurrence(2);

        Assert.True(removed);
        Assert.Equal(new List<int> { 1, 3 }, ToList(list));
    }

    [Fact]
    public void RemoveFirstOccurrence_NonExistingValue_ReturnsFalse()
    {
        var list = new DoublyLinkedList<int>(new[] { 1, 2, 3 });

        var removed = list.RemoveFirstOccurrence(99);

        Assert.False(removed);
        Assert.Equal(new List<int> { 1, 2, 3 }, ToList(list));
    }

    // Clear ------------------------------------------------

    [Fact]
    public void Clear_EmptiesList()
    {
        var list = new DoublyLinkedList<int>(new[] { 1, 2, 3 });

        list.Clear();

        Assert.True(list.IsEmpty);
        Assert.Equal(0, list.Count);
        Assert.Empty(ToList(list));
        Assert.Throws<InvalidOperationException>(() => list.PeekFirst());
        Assert.Throws<InvalidOperationException>(() => list.PeekLast());
    }

    // Iteration --------------------------------------------

    [Fact]
    public void Iterator_TraversesInOrder()
    {
        var list = new DoublyLinkedList<int>(new[] { 1, 2, 3 });

        Assert.Equal(new List<int> { 1, 2, 3 }, ToList(list));
    }

    [Fact]
    public void AsReversed_TraversesInReverseOrder()
    {
        var list = new DoublyLinkedList<int>(new[] { 1, 2, 3 });

        Assert.Equal(new List<int> { 3, 2, 1 }, ToReversedList(list));
    }

    // ToString ---------------------------------------------

    [Fact]
    public void ToString_ContainsValues()
    {
        var list = new DoublyLinkedList<int>(new[] { 1, 2, 3 });

        var s = list.ToString();

        Assert.StartsWith("DoublyLinkedList[", s);
        Assert.Contains("1", s);
        Assert.Contains("2", s);
        Assert.Contains("3", s);
        Assert.EndsWith("]", s);
    }
}
