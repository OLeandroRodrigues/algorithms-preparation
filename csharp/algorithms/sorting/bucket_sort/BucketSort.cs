using System;
using System.Collections.Generic;

namespace Algorithms.Sorting;

public static class BucketSort
{
    public static void Sort(double[] arr)
    {
        int n = arr == null ? 0 : arr.Length;
        if (n <= 1)
            return;

        var buckets = new List<List<double>>(n);
        for (int i = 0; i < n; i++)
            buckets.Add(new List<double>());

        foreach (double value in arr)
        {
            int index = (int)Math.Floor(value * n);
            if (index == n) index = n - 1; // Clamp for value == 1.0
            buckets[index].Add(value);
        }

        foreach (var bucket in buckets)
            InsertionSort(bucket);

        int pos = 0;
        foreach (var bucket in buckets)
            foreach (double value in bucket)
                arr[pos++] = value;
    }

    private static void InsertionSort(List<double> list)
    {
        for (int i = 1; i < list.Count; i++)
        {
            double key = list[i];
            int j = i - 1;

            while (j >= 0 && list[j] > key)
            {
                list[j + 1] = list[j];
                j--;
            }
            list[j + 1] = key;
        }
    }

    public static void Sort(int[] arr)
    {
        int n = arr == null ? 0 : arr.Length;
        if (n <= 1)
            return;

        int min = arr[0], max = arr[0];
        for (int i = 1; i < n; i++)
        {
            if (arr[i] < min) min = arr[i];
            if (arr[i] > max) max = arr[i];
        }

        if (min == max)
            return; // already "sorted"

        int bucketCount = Math.Max(1, n);
        double range = max - min + 1;

        var buckets = new List<List<int>>(bucketCount);
        for (int i = 0; i < bucketCount; i++)
            buckets.Add(new List<int>());

        foreach (int value in arr)
        {
            double norm = (value - min) / range;
            int index = (int)Math.Floor(norm * bucketCount);
            if (index == bucketCount) index = bucketCount - 1;
            buckets[index].Add(value);
        }

        foreach (var bucket in buckets)
            bucket.Sort();

        int pos = 0;
        foreach (var bucket in buckets)
            foreach (int value in bucket)
                arr[pos++] = value;
    }
}

