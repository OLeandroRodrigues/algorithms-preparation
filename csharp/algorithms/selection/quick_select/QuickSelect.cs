using System;
namespace Selection;

public static class QuickSelect
{
    private static readonly Random random = new Random();

    public static int QuickSelectAlgorithm(int[] arr, int low, int high, int k)
    {
        if (k < 1 || k > (high - low + 1))
            throw new IndexOutOfRangeException("k out of range");

        if (low == high)
            return arr[low];

        if (low < high)
        {
            int pivotIndex = random.Next(low, high + 1); // random index between low and high
            Swap(arr, pivotIndex, high);

            int p = Partition(arr, low, high);
            int pos = p - low + 1;

            if (pos == k)
                return arr[p];
            else if (pos > k)
                return QuickSelectAlgorithm(arr, low, p - 1, k);
            else
                return QuickSelectAlgorithm(arr, p + 1, high, k - pos);
        }

        throw new InvalidOperationException("Unexpected state in QuickSelectAlgorithm");
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

    // Example usage
    /*public static void Main(string[] args)
    {
        int[] nums = { 7, 10, 4, 3, 20, 15 };
        int k = 3;
        int result = QuickSelectAlgorithm(nums, 0, nums.Length - 1, k);
        Console.WriteLine($"{k}-th smallest element is {result}");
    }*/
}
