package sorting;

import java.util.Arrays;

public class RadixSort {

    private static void countingSortForRadix(int[] arr, int exp) {
        int n = arr.length;
        int[] output = new int[n];
        int[] count = new int[10]; // For base 10 digits (0-9)

        // Count occurrences of each digit
        for (int num : arr) {
            int index = (num / exp) % 10;
            count[index]++;
        }

        // Prefix sums (cumulative count)
        for (int i = 1; i < 10; i++) {
            count[i] += count[i - 1];
        }

        // Build the output array (stable)
        for (int i = n - 1; i >= 0; i--) {
            int index = (arr[i] / exp) % 10;
            output[count[index] - 1] = arr[i];
            count[index]--;
        }

        // Copy output to original array
        for (int i = 0; i < n; i++) {
            arr[i] = output[i];
        }
    }

    // ---------- Radix Sort ----------
    public static void radixSort(int[] arr) {
        if (arr == null || arr.length == 0) return;

        int maxVal = findMax(arr);
        int exp = 1;
        int step = 1;

        while (maxVal / exp > 0) {
            System.out.println("\n--- Pass " + step + " ---");
            System.out.println("exp = " + exp);
            System.out.println("max_val // exp = " + (maxVal / exp));
            System.out.println("Digit being processed: " + exp + " (1=units,10=tens,100=hundreds...)");

            countingSortForRadix(arr, exp);
            System.out.println("Array after sorting by digit " + exp + ": " + Arrays.toString(arr));

            exp *= 10;
            step++;
        }
    }

    // ---------- Helper: find max value ----------
    private static int findMax(int[] arr) {
        int max = arr[0];
        for (int num : arr) {
            if (num > max) max = num;
        }
        return max;
    }

    // ---------- Example of use ----------
    public static void main(String[] args) {
        int[] data = {329, 457, 657, 839, 436, 720, 355};
        System.out.println("Before: " + Arrays.toString(data));
        radixSort(data);
        System.out.println("\nAfter:  " + Arrays.toString(data));
    }
}

