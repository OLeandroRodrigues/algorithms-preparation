using System;
using System.Threading;
using DataStructure.Generic.Heap;

namespace DataStructure.PriorityQueue.Custom;

/// <summary>
/// Priority Queue implementation using a custom MaxHeap.
/// 
/// Each element is stored as a <see cref="PriorityItem{T}"/> (priority, -order, value) to ensure:
/// - Higher priority values are served first (max-priority behavior)
/// - FIFO stability among elements with the same priority (via negative order)
/// 
/// Time Complexity:
/// - Push(): O(log n)
/// - Pop():  O(log n)
/// - Peek(): O(1)
/// - IsEmpty(), Size(): O(1)
/// </summary>
public class PriorityQueueCustom<T>
{
    private readonly MaxHeap<PriorityItem<T>> _heap;
    private long _counter; 

    public PriorityQueueCustom()
    {
        _heap = new MaxHeap<PriorityItem<T>>();
        _counter = 0;
    }


    public void Push(T value, int priority)
    {
        long order = Interlocked.Increment(ref _counter);
        _heap.Insert(new PriorityItem<T>(priority, -order, value));
    }

    public T Pop()
    {
        if (IsEmpty())
            throw new InvalidOperationException("Pop from an empty priority queue");

        var item = _heap.Pop();
        return item.Value;
    }

    public T Peek()
    {
        if (IsEmpty())
            throw new InvalidOperationException("Peek from an empty priority queue");

        return _heap.Peek().Value;
    }

    public bool IsEmpty() => Size() == 0;

    public int Size() => _heap.Size();

    private sealed class PriorityItem<TValue> : IComparable<PriorityItem<TValue>>
    {
        public int Priority { get; }
        public long NegOrder { get; }
        public TValue Value { get; }

        public PriorityItem(int priority, long negOrder, TValue value)
        {
            Priority = priority;
            NegOrder = negOrder;
            Value = value;
        }

        public int CompareTo(PriorityItem<TValue> other)
        {
            if (other == null) return 1;

            int cmp = Priority.CompareTo(other.Priority);
            if (cmp != 0)
                return cmp;
            return NegOrder.CompareTo(other.NegOrder);
        }

        public override string ToString() => $"({Priority}, {NegOrder}, {Value})";
    }
}
