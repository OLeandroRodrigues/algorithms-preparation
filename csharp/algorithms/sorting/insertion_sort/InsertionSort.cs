namespace Algorithms.Sorting;

/// <summary>
/// Insertion Sort (in-place).
/// Time: O(n^2) worst/avg, O(n) best. Space: O(1)
/// Proof: see algorithms/sorting/insertion_sort/README.md
/// </summary>
public static class InsertionSort
{
    public static void Sort(int[] arr)
    {
        for (int i = 1; i < arr.Length; i++)
        {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key)
            {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }
}