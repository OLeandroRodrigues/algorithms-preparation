using System;

namespace Algorithms.Sorting;

public static class HeapSortInPlace
{
    // Function to maintain the max-heap property
    private static void Heapify(int[] arr, int n, int i)
    {
        int largest = i;           // root
        int left = 2 * i + 1;      // left child
        int right = 2 * i + 2;     // right child

        // If left child is larger than root
        if (left < n && arr[left] > arr[largest])
        {
            largest = left;
        }

        // If right child is larger than the largest so far
        if (right < n && arr[right] > arr[largest])
        {
            largest = right;
        }

        // If the largest is not root
        if (largest != i)
        {
            // Swap arr[i] with arr[largest]
            int temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;

            // Recursively heapify the affected sub-tree
            Heapify(arr, n, largest);
        }
    }

    // Heap sort function
    public static void HeapSort(int[] arr)
    {
        int n = arr.Length;

        // Step 1: Build a max heap
        for (int i = n / 2 - 1; i >= 0; i--)
        {
            Heapify(arr, n, i);
        }

        // Step 2: Extract elements one by one
        for (int end = n - 1; end > 0; end--)
        {
            // Move current root (max element) to the end
            int temp = arr[0];
            arr[0] = arr[end];
            arr[end] = temp;

            // Call heapify on the reduced heap
            Heapify(arr, end, 0);
        }
    }

    // Demo
    /*public static void Main(string[] args)
    {
        int[] A = { 7, 51, 4, 10, 15, 30, 50 };
        HeapSort(A);
        Console.WriteLine("Sorted ascending: " + string.Join(", ", A));
        // Output: 4, 7, 10, 15, 30, 50, 51
    }*/
}
