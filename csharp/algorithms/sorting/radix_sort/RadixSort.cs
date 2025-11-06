using System;

namespace Algorithms.Sorting;

public static class RadixSort
{
    private static void CountingSortForRadix(int[] arr, int exp)
    {
        int n = arr.Length;
        int[] output = new int[n];
        int[] count = new int[10]; // dígitos 0-9

        for (int i = 0; i < n; i++)
        {
            int index = (arr[i] / exp) % 10;
            count[index]++;
        }

        for (int i = 1; i < 10; i++)
            count[i] += count[i - 1];

        for (int i = n - 1; i >= 0; i--)
        {
            int index = (arr[i] / exp) % 10;
            output[count[index] - 1] = arr[i];
            count[index]--;
        }

        for (int i = 0; i < n; i++)
            arr[i] = output[i];
    }

    public static void Sort(int[] arr, bool verbose = true)
    {
        if (arr == null || arr.Length == 0) return;

        int maxVal = FindMax(arr);
        int exp = 1;
        int step = 1;

        while (maxVal / exp > 0)
        {
            if (verbose)
            {
                Console.WriteLine($"\n--- Pass {step} ---");
                Console.WriteLine($"exp = {exp}");
                Console.WriteLine($"max_val // exp = {maxVal / exp}");
                Console.WriteLine($"Digit being processed: {exp} (1=units,10=tens,100=hundreds...)");
            }

            CountingSortForRadix(arr, exp);

            if (verbose)
                Console.WriteLine($"Array after sorting by digit {exp}: [{string.Join(", ", arr)}]");

            exp *= 10;
            step++;
        }
    }

    private static int FindMax(int[] arr)
    {
        int max = arr[0];
        for (int i = 1; i < arr.Length; i++)
            if (arr[i] > max) max = arr[i];
        return max;
    }
}