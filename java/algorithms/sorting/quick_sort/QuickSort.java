package sorting;

public final class QuickSort {

    private QuickSort() {}

    public static int[] quickSort(int[] arr) {
        if (arr == null || arr.length <= 1)
            return arr;

        quickSort(arr, 0, arr.length - 1);
        return arr;
    }

    private static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int p = partition(arr, low, high);
            quickSort(arr, low, p - 1);
            quickSort(arr, p + 1, high);
        }
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

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    // Sample of use 
    public static void main(String[] args) {
        int[] A = {2, 8, 7, 1, 3, 5, 6};
        System.out.println("Before: ");
        printArray(A);

        quickSort(A);

        System.out.println("After: ");
        printArray(A);
    }

    private static void printArray(int[] arr) {
        for (int n : arr) {
            System.out.print(n + " ");
        }
        System.out.println();
    }
}