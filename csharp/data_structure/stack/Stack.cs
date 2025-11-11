
using System;
using System.Collections.Generic;

namespace DataStructure.Stack;

public class Stack<T>
{
    private readonly List<T> _items;

    public Stack()
    {
        _items = new List<T>();
    }

    public void Push(T item) => _items.Add(item);
    public T Pop()
    {
        if (IsEmpty())
            throw new InvalidOperationException("pop from empty stack");

        int lastIndex = _items.Count - 1;
        T value = _items[lastIndex];
        _items.RemoveAt(lastIndex);
        return value;
    }

    public T Peek()
    {
        if (IsEmpty())
            throw new InvalidOperationException("peek from empty stack");

        return _items[^1]; // same as _items[_items.Count - 1]
    }

    public bool IsEmpty() => _items.Count == 0;

    public int Size() => _items.Count;

    public override string ToString() => $"Stack({_items.Count} elements)";
}

