using System;
using System.Collections.Generic;

namespace DataStructure.Generic.Heap;

public class MaxHeap<T> where T : IComparable<T>
{
    private readonly List<T> data = new List<T>();

    // --- Public API ---
    public void Insert(T value)
    {
        data.Add(value);
        HeapifyUp(data.Count - 1);
    }

    public T Pop()
    {
        if (data.Count == 0)
            throw new InvalidOperationException("Heap is empty");

        T root = data[0];
        int lastIdx = data.Count - 1;

        Swap(0, lastIdx);
        data.RemoveAt(lastIdx);

        if (data.Count > 0)
            HeapifyDown(0);

        return root;
    }

    public T Peek()
    {
        if (data.Count == 0)
            throw new InvalidOperationException("Heap is empty");
        return data[0];
    }

    public int Size() => data.Count;

    public bool IsEmpty() => data.Count == 0;

    // --- Internals ---
    private static int Parent(int i) => (i - 1) / 2;
    private static int Left(int i) => 2 * i + 1;
    private static int Right(int i) => 2 * i + 2;

    private void HeapifyUp(int i)
    {
        while (i > 0)
        {
            int p = Parent(i);
            if (data[i].CompareTo(data[p]) <= 0) break;
            Swap(i, p);
            i = p;
        }
    }

    private void HeapifyDown(int i)
    {
        int n = data.Count;
        while (Left(i) < n)
        {
            int l = Left(i), r = Right(i);
            int largest = i;

            if (data[l].CompareTo(data[largest]) > 0) largest = l;
            if (r < n && data[r].CompareTo(data[largest]) > 0) largest = r;

            if (largest == i) break;
            Swap(i, largest);
            i = largest;
        }
    }

    private void Swap(int i, int j)
    {
        T tmp = data[i];
        data[i] = data[j];
        data[j] = tmp;
    }
}
