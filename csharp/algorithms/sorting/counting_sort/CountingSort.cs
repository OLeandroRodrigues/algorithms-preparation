using System;
namespace Algorithms.Sorting;

public static class CountingSort
{
    public static int[] Sort(int[] arr)
    {
        if (arr == null || arr.Length == 0)
            return Array.Empty<int>();

        int k = FindMax(arr);

        int[] C = new int[k + 1];

        foreach (int value in arr)
            C[value]++;

        for (int i = 1; i <= k; i++)
            C[i] += C[i - 1];

        int[] B = new int[arr.Length];

        for (int j = arr.Length - 1; j >= 0; j--)
        {
            int x = arr[j];
            C[x]--;            
            int pos = C[x];
            B[pos] = x;
        }

        return B;
    }

    private static int FindMax(int[] arr)
    {
        int max = arr[0];
        foreach (int v in arr)
        {
            if (v > max) max = v;
        }
        return max;
    }

    // Example of use
    /*public static void Main(string[] args)
    {
        int[] data = { 4, 2, 2, 8, 3, 3, 1 };
        int[] sorted = Sort(data);

        Console.WriteLine("[" + string.Join(", ", sorted) + "]");
        // Expected output: [1, 2, 2, 3, 3, 4, 8]
    }*/
}

