package sorting;
import java.util.Arrays;

public class CountingSort {

    public static int[] countingSort(int[] arr) {
        
        if (arr == null || arr.length == 0) {
            return new int[0];
        }

        int k = findMax(arr);

        int[] C = new int[k + 1];

        for (int value : arr) {
            C[value]++;
        }

        for (int i = 1; i <= k; i++) {
            C[i] += C[i - 1];
        }

        int[] B = new int[arr.length];

        for (int j = arr.length - 1; j >= 0; j--) {
            int x = arr[j];
            C[x]--;              
            int pos = C[x];      
            B[pos] = x;
        }

        return B;
    }

    private static int findMax(int[] arr) {
        int max = arr[0];
        for (int v : arr) {
            if (v > max) max = v;
        }
        return max;
    }

    // Sample of use
    public static void main(String[] args) {
        int[] data = {4, 2, 2, 8, 3, 3, 1};
        int[] sorted = countingSort(data);
        System.out.println(Arrays.toString(sorted));
        // Output expected: [1, 2, 2, 3, 3, 4, 8]
    }
}