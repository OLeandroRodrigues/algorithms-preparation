package sorting;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public final class BucketSort {

    private BucketSort() {  }

    public static void bucketSort(double[] arr) {
        int n = arr == null ? 0 : arr.length;
        if (n <= 1) return; 

        List<List<Double>> buckets = new ArrayList<>(n);
        for (int i = 0; i < n; i++) buckets.add(new ArrayList<>());

        for (double v : arr) {
            int index = (int) Math.floor(v * n);
            if (index == n) index = n - 1; 
            buckets.get(index).add(v);
        }

        for (List<Double> b : buckets) {
            insertionSort(b);
        }

        int pos = 0;
        for (List<Double> b : buckets) {
            for (double v : b) arr[pos++] = v;
        }
    }

    private static void insertionSort(List<Double> list) {
        for (int i = 1; i < list.size(); i++) {
            double key = list.get(i);
            int j = i - 1;
            // move elements greater than key to one position ahead
            while (j >= 0 && list.get(j) > key) {
                // shift to the right
                if (j + 1 < list.size()) {
                    list.set(j + 1, list.get(j));
                }
                j--;
            }
            list.set(j + 1, key);
        }
    }

    public static void bucketSortInts(int[] arr) {
        int n = arr == null ? 0 : arr.length;
        if (n <= 1) return;

        int min = arr[0], max = arr[0];
        for (int v : arr) {
            if (v < min) min = v;
            if (v > max) max = v;
        }
        if (min == max) return; // already "sorted" (all equal)

        // number of buckets ~ n (common heuristic)
        int bucketCount = Math.max(1, n);
        double range = (double) (max - min + 1);

        List<List<Integer>> buckets = new ArrayList<>(bucketCount);
        for (int i = 0; i < bucketCount; i++) buckets.add(new ArrayList<>());

        // map each value to a bucket index in [0, bucketCount-1]
        for (int v : arr) {
            // normalized position in [0, 1)
            double norm = (v - min) / range; // range includes +1 to cover max
            int index = (int) Math.floor(norm * bucketCount);
            if (index == bucketCount) index = bucketCount - 1; // clamp for v == max
            buckets.get(index).add(v);
        }

        // sort each bucket (for ints, Java's stable sort for small lists is fine;
        // it is possible to implement insertionSort for integers similarly)
        for (List<Integer> b : buckets) {
            // Using Collections.sort (Timsort) is stable and efficient for small buckets
            Collections.sort(b);
        }

        // concatenate
        int pos = 0;
        for (List<Integer> b : buckets) {
            for (int v : b) arr[pos++] = v;
        }
    }

    // ------------------------------------------------------------
    // example usage
    // ------------------------------------------------------------
    public static void main(String[] args) {
        double[] a = {0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51, 1.0};
        System.out.println("Before (double):");
        for (double v : a) System.out.print(v + " ");
        System.out.println();

        bucketSort(a);

        System.out.println("After  (double):");
        for (double v : a) System.out.print(v + " ");
        System.out.println();

        int[] b = {12, 5, 7, 7, 20, 1, 15, 3, 3, 100};
        System.out.println("Before (int):");
        for (int v : b) System.out.print(v + " ");
        System.out.println();

        bucketSortInts(b);

        System.out.println("After  (int):");
        for (int v : b) System.out.print(v + " ");
        System.out.println();
    }
}