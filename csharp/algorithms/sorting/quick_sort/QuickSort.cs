namespace Algorithms.Sorting;

public static class QuickSort
{
    public static int[] Sort(int[] arr)
    {
        if (arr == null || arr.Length <= 1)
            return arr;

        QuickSortRecursive(arr, 0, arr.Length - 1);
        return arr;
    }

    private static void QuickSortRecursive(int[] arr, int low, int high)
    {
        if (low < high)
        {
            int p = Partition(arr, low, high);
            QuickSortRecursive(arr, low, p - 1);
            QuickSortRecursive(arr, p + 1, high);
        }
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

    public static void PrintArray(int[] arr)
    {
        Console.WriteLine(string.Join(" ", arr));
    }

    /*
    public static void Main(string[] args)
    {
        int[] arr = { 2, 8, 7, 1, 3, 5, 6 };
        Console.WriteLine("Before:");
        PrintArray(arr);

        Sort(arr);

        Console.WriteLine("After:");
        PrintArray(arr);
    }*/
}
