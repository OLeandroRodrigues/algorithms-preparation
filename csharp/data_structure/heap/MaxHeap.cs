using System;
using System.Collections.Generic;

namespace DataStructure.Heap;

public class MaxHeap
{
    private readonly List<int> data = new List<int>();

    // --- Public API ---
    public void Insert(int value)
    {
        data.Add(value);
        HeapifyUp(data.Count - 1);
    }

    public int Pop()
    {
        if (data.Count == 0) throw new InvalidOperationException("Heap is empty");

        int root = data[0];
        int lastIdx = data.Count - 1;

        // Move last to root, remove tail, then restore heap property
        Swap(0, lastIdx);
        data.RemoveAt(lastIdx);

        if (data.Count > 0)
            HeapifyDown(0);

        return root;
    }

    public int Peek()
    {
        if (data.Count == 0) throw new InvalidOperationException("Heap is empty");
        return data[0];
    }

    public int Size()
    {
        return data.Count;
    }

    // --- Internals ---
    private static int Parent(int i) => (i - 1) / 2;
    private static int Left(int i) => 2 * i + 1;
    private static int Right(int i) => 2 * i + 2;

    private void HeapifyUp(int i)
    {
        while (i > 0)
        {
            int p = Parent(i);
            if (data[i] <= data[p]) break;
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

            if (data[l] > data[largest]) largest = l;
            if (r < n && data[r] > data[largest]) largest = r;

            if (largest == i) break;
            Swap(i, largest);
            i = largest;
        }
    }

    private void Swap(int i, int j)
    {
        int tmp = data[i];
        data[i] = data[j];
        data[j] = tmp;
    }
}
