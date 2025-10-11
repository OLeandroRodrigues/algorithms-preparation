using System;
using System.Collections.Generic;
using System.Threading;

namespace DataStructure.PriorityQueue.Builtin;

/// <summary>
/// Priority Queue implemented using .NET's built-in PriorityQueue&lt;TElement, TPriority&gt;.
///
/// Features:
/// - Supports Min or Max behavior (configurable via constructor)
/// - Stable among equal priorities (FIFO) using a monotonic counter
///
/// Time Complexity:
/// - Push(): O(log n)
/// - Pop():  O(log n)
/// - Peek(): O(1)
/// - Size(), IsEmpty(): O(1)
/// </summary>
public class PriorityQueueBuiltin<T>
{
    private readonly PriorityQueue<QueueItem<T>, (int priority, long order)> _pq;
    private readonly bool _isMin;
    private long _counter;

    public PriorityQueueBuiltin(bool isMin = true)
    {
        _isMin = isMin;
        _pq = new PriorityQueue<QueueItem<T>, (int priority, long order)>();
        _counter = 0;
    }

    public void Push(T value, int priority)
    {
        long order = Interlocked.Increment(ref _counter);

        // For stability and direction:
        // - Min-queue: smaller priority first, then smaller order first
        // - Max-queue: invert priority to negative so that "larger" comes first
        var effectivePriority = _isMin ? priority : -priority;
        var item = new QueueItem<T>(value, priority, order);
        _pq.Enqueue(item, (effectivePriority, order));
    }

    public T Pop()
    {
        if (_pq.Count == 0)
            throw new InvalidOperationException("Pop from an empty priority queue");

        return _pq.Dequeue().Value;
    }

    public T Peek()
    {
        if (_pq.Count == 0)
            throw new InvalidOperationException("Peek from an empty priority queue");

        return _pq.Peek().Value;
    }

    public int Size() => _pq.Count;
    public bool IsEmpty() => _pq.Count == 0;
    public void Clear() => _pq.Clear();

    // --- Internal node class ---
    private sealed class QueueItem<TValue>
    {
        public TValue Value { get; }
        public int OriginalPriority { get; }
        public long Order { get; }

        public QueueItem(TValue value, int priority, long order)
        {
            Value = value;
            OriginalPriority = priority;
            Order = order;
        }

        public override string ToString() => $"({OriginalPriority}, {Order}, {Value})";
    }
}
