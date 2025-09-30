using System;
using System.Collections.Generic;
using DataStructure.Heap;

namespace Algorithms.Sorting;

public static class HeapSort
{
    public static List<int> SortDesc(List<int> arr)
    {
        // Sorts in descending order by reusing MaxHeap:
        // inserts all elements and repeatedly pops the max (largest -> smallest).
        var heap = new MaxHeap();
        foreach (var item in arr)
        {
            heap.Insert(item);
        }

        var result = new List<int>();
        while (heap.Size() != 0)
        {
            result.Add(heap.Pop());
        }
        return result;
    }

    public static List<int> SortAsc(List<int> arr)
    {
        // Sorts in ascending order using the same MaxHeap:
        // obtains the descending list and then reverses it.
        var desc = SortDesc(arr);
        desc.Reverse();
        return desc;
    }

    /* Demo */
    /*public static void Main(string[] args)
    {
        var A = new List<int> { 4, 5, 5, 10, 10, 8, 2, 100, 50, 30, 1 };

        Console.WriteLine("Asc : " + string.Join(", ", HeapSort.SortAsc(A)));
        // [1, 2, 4, 5, 5, 8, 10, 10, 30, 50, 100]

        Console.WriteLine("Desc: " + string.Join(", ", HeapSort.SortDesc(A)));
        // [100, 50, 30, 10, 10, 8, 5, 5, 4, 2, 1]
    }*/
}
