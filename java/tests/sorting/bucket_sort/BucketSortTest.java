package sorting;

import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.Random;
import static org.junit.jupiter.api.Assertions.*;


public class BucketSortTest {

    // ------------------------------------------------------------
    // helper methods
    // ------------------------------------------------------------
    private static boolean isSorted(double[] arr) {
        for (int i = 1; i < arr.length; i++)
            if (arr[i - 1] > arr[i]) return false;
        return true;
    }

    private static boolean isSorted(int[] arr) {
        for (int i = 1; i < arr.length; i++)
            if (arr[i - 1] > arr[i]) return false;
        return true;
    }

    // ------------------------------------------------------------
    // tests for double version
    // ------------------------------------------------------------

    @Test
    void testEmptyArray() {
        double[] arr = {};
        BucketSort.bucketSort(arr);
        assertEquals(0, arr.length);
    }

    @Test
    void testSingleElement() {
        double[] arr = {0.42};
        BucketSort.bucketSort(arr);
        assertEquals(0.42, arr[0], 1e-9);
    }

    @Test
    void testAlreadySorted() {
        double[] arr = {0.1, 0.2, 0.3, 0.4, 0.5};
        BucketSort.bucketSort(arr);
        assertTrue(isSorted(arr));
    }

    @Test
    void testReversedArray() {
        double[] arr = {0.9, 0.8, 0.7, 0.6, 0.5, 0.4};
        BucketSort.bucketSort(arr);
        assertTrue(isSorted(arr));
    }

    @Test
    void testWithDuplicates() {
        double[] arr = {0.5, 0.5, 0.1, 0.1, 0.3, 0.3};
        BucketSort.bucketSort(arr);
        assertTrue(isSorted(arr));
        assertArrayEquals(new double[]{0.1, 0.1, 0.3, 0.3, 0.5, 0.5}, arr, 1e-9);
    }

    @Test
    void testBoundaryValueOne() {
        double[] arr = {0.0, 1.0, 0.9999, 0.1234};
        BucketSort.bucketSort(arr);
        assertTrue(isSorted(arr));
        assertEquals(4, arr.length);
    }

    @Test
    void testRandomInput() {
        Random rng = new Random(42);
        double[] arr = new double[1000];
        for (int i = 0; i < arr.length; i++)
            arr[i] = rng.nextDouble(); // in [0,1)
        BucketSort.bucketSort(arr);
        assertTrue(isSorted(arr));
    }

    @Test
    void testPrecisionEdges() {
        double[] arr = {0.0, 0.1666666, 0.1666667, 0.3333333, 0.3333334, 0.5, 0.6666666, 0.6666667, 0.9999999};
        BucketSort.bucketSort(arr);
        assertTrue(isSorted(arr));
    }

    // ------------------------------------------------------------
    // tests for integer version
    // ------------------------------------------------------------

    @Test
    void testIntegersAlreadySorted() {
        int[] arr = {1, 2, 3, 4, 5};
        BucketSort.bucketSortInts(arr);
        assertTrue(isSorted(arr));
    }

    @Test
    void testIntegersReversed() {
        int[] arr = {9, 7, 5, 3, 1};
        BucketSort.bucketSortInts(arr);
        assertTrue(isSorted(arr));
        assertArrayEquals(new int[]{1, 3, 5, 7, 9}, arr);
    }

    @Test
    void testIntegersWithDuplicates() {
        int[] arr = {5, 3, 5, 3, 1};
        BucketSort.bucketSortInts(arr);
        assertTrue(isSorted(arr));
        assertArrayEquals(new int[]{1, 3, 3, 5, 5}, arr);
    }

    @Test
    void testIntegersWithNegatives() {
        int[] arr = {-5, -1, -10, 0, 2, 2};
        BucketSort.bucketSortInts(arr);
        assertTrue(isSorted(arr));
        assertArrayEquals(new int[]{-10, -5, -1, 0, 2, 2}, arr);
    }

    @Test
    void testIntegersRandomReproducible() {
        Random rng = new Random(123);
        int[] arr = new int[1000];
        for (int i = 0; i < arr.length; i++)
            arr[i] = rng.nextInt(1000); // [0,1000)
        int[] expected = arr.clone();
        Arrays.sort(expected);

        BucketSort.bucketSortInts(arr);
        assertArrayEquals(expected, arr);
    }

    @Test
    void testIntegersAllEqual() {
        int[] arr = {7, 7, 7, 7, 7};
        BucketSort.bucketSortInts(arr);
        assertArrayEquals(new int[]{7, 7, 7, 7, 7}, arr);
    }

    @Test
    void testIntegersLargeRange() {
        int[] arr = {1000, -5000, 300, 0, 1500, 9999};
        int[] expected = arr.clone();
        Arrays.sort(expected);

        BucketSort.bucketSortInts(arr);
        assertArrayEquals(expected, arr);
        assertTrue(isSorted(arr));
    }
}
