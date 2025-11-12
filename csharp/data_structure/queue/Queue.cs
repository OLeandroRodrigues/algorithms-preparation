using System;
using System.Collections.Generic;

namespace DataStructure.Queue;

public class Queue<T>
{
    private readonly LinkedList<T> _items = new();

    public void Enqueue(T item)
    {
        _items.AddLast(item);
    }

    public T Dequeue()
    {
        if (IsEmpty())
            throw new InvalidOperationException("Dequeue from empty queue");

        T value = _items.First.Value;
        _items.RemoveFirst();
        return value;
    }

    public T Peek()
    {
        if (IsEmpty())
            throw new InvalidOperationException("Peek from empty queue");

        return _items.First.Value;
    }

    public bool IsEmpty() => _items.Count == 0;

    public int Size() => _items.Count;

    public override string ToString() => $"Queue({string.Join(", ", _items)})";
}

