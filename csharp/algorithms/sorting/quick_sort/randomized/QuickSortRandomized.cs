using System;

namespace Algorithms.Sorting.QuickSortRandomized;

public static class QuickSortRandomized
{
    private static readonly Random _rand = new Random();

    public static void QuickSort(int[] arr, int low, int high)
    {
        if (low < high)
        {
            int p = RandomizedPartition(arr, low, high);

            // recursive calls
            QuickSort(arr, low, p - 1);   // left side
            QuickSort(arr, p + 1, high);  // right side
        }
    }

    private static int RandomizedPartition(int[] arr, int low, int high)
    {
        // random between [low, high]
        int pivotIndex = _rand.Next(low, high + 1);
        Swap(arr, pivotIndex, high);
        return Partition(arr, low, high);
    }

    private static int Partition(int[] arr, int low, int high)
    {
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++)
        {
            if (arr[j] <= pivot)
            {
                i++;
                Swap(arr, i, j);
            }
        }

        Swap(arr, i + 1, high);
        return i + 1;
    }

    private static void Swap(int[] arr, int i, int j)
    {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    // Sample usage / entry point
    /*public static void Main(string[] args)
    {
        int[] A = { 2, 8, 7, 1, 3, 5, 6 };

        Console.WriteLine("Before:");
        PrintArray(A);

        QuickSort(A, 0, A.Length - 1);

        Console.WriteLine("After:");
        PrintArray(A);
    }

    private static void PrintArray(int[] arr)
    {
        foreach (int x in arr)
            Console.Write(x + " ");
        Console.WriteLine();
    }*/
}
