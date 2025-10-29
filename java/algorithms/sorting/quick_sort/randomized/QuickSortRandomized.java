package algorithms.sorting.quick_sort.randomized;
import java.util.Random;


public class QuickSortRandomized {

    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int p = randomizedPartition(arr, low, high);

            // recursive calls
            quickSort(arr, low, p - 1);   // left side
            quickSort(arr, p + 1, high);  // right side
        }
    }

    private static int randomizedPartition(int[] arr, int low, int high) {
        Random rand = new Random();
        int pivotIndex = rand.nextInt(high - low + 1) + low; // random between low and high
        swap(arr, pivotIndex, high);
        return partition(arr, low, high);
    }

    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i + 1, high);
        return i + 1;
    }

    // Swap helper method
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    // Sample usage
    public static void main(String[] args) {
        int[] A = {2, 8, 7, 1, 3, 5, 6};
        System.out.println("Before: ");
        printArray(A);

        quickSort(A, 0, A.length - 1);

        System.out.println("After: ");
        printArray(A);
    }

    // Helper to print arrays
    private static void printArray(int[] arr) {
        for (int x : arr) {
            System.out.print(x + " ");
        }
        System.out.println();
    }
}