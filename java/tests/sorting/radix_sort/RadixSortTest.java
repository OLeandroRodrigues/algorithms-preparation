package sorting;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Disabled;

import java.util.Arrays;
import java.util.Random;

import static org.junit.jupiter.api.Assertions.*;

public class RadixSortTest {

    private static void assertSortedEqualsJavaSort(int[] arr) {
        int[] expected = Arrays.copyOf(arr, arr.length);
        Arrays.sort(expected);
        RadixSort.radixSort(arr);
        assertArrayEquals(expected, arr);
    }

    @Test
    @DisplayName("Empty array")
    void testEmpty() {
        int[] arr = {};
        RadixSort.radixSort(arr);
        assertArrayEquals(new int[]{}, arr);
        System.out.println("Empty array: OK");
    }

    @Test
    @DisplayName("Single element")
    void testSingle() {
        int[] arr = {42};
        RadixSort.radixSort(arr);
        assertArrayEquals(new int[]{42}, arr);
        System.out.println("Single element: OK");
    }

    @Test
    @DisplayName("Already sorted")
    void testAlreadySorted() {
        int[] arr = {1, 2, 3, 4, 5, 6};
        int[] expected = Arrays.copyOf(arr, arr.length);
        RadixSort.radixSort(arr);
        assertArrayEquals(expected, arr);
        System.out.println("Already sorted: OK");
    }

    @Test
    @DisplayName("Reverse sorted")
    void testReverseSorted() {
        int[] arr = {9, 8, 7, 6, 5, 4, 3, 2, 1};
        assertSortedEqualsJavaSort(arr);
        System.out.println("Reverse sorted: OK");
    }

    @Test
    @DisplayName("With duplicates")
    void testWithDuplicates() {
        int[] arr = {5, 3, 5, 2, 9, 3, 2, 2, 8, 5};
        assertSortedEqualsJavaSort(arr);
        System.out.println("With duplicates: OK");
    }

    @Test
    @DisplayName("Contains zero")
    void testContainsZero() {
        int[] arr = {0, 3, 0, 2, 1, 0, 9};
        assertSortedEqualsJavaSort(arr);
        System.out.println("Contains zero: OK");
    }

    @Test
    @DisplayName("Random small (reproducible)")
    void testRandomSmallReproducible() {
        Random rng = new Random(1337);
        int[] arr = rng.ints(2_000, 0, 10_000).toArray();
        assertSortedEqualsJavaSort(arr);
        System.out.println("Random small (2k items): OK");
    }

    @Test
    @DisplayName("Random medium (reproducible)")
    void testRandomMediumReproducible() {
        Random rng = new Random(2025);
        int[] arr = rng.ints(20_000, 0, 1_000_000).toArray();
        assertSortedEqualsJavaSort(arr);
        System.out.println("Random medium (20k items): OK");
    }

    @Test
    @DisplayName("Large digits values")
    void testLargeDigitsValues() {
        int[] arr = {1_000_000_007, 1_000_000, 1_000_000_000, 0, 1_000_000_001, 999_999_999};
        assertSortedEqualsJavaSort(arr);
        System.out.println("Large digits values: OK");
    }

    @Test
    @DisplayName("CPF-like (11 digits as integers)")
    void testCpfLikeValues() {
        Random rng = new Random(111);
        // values until 11 digits (0 .. 99_999_999_999 não cabe em int) => use until 2_147_483_647 (int)
        int[] arr = rng.ints(3_000, 0, Integer.MAX_VALUE).toArray();
        assertSortedEqualsJavaSort(arr);
        System.out.println("CPF-like (3k items): OK");
    }

    @Disabled("RadixSort current doesn't consider negative number. Able it when add validation/strategy.")
    @Test
    @DisplayName("Negatives not supported (by design) – pending behavior decision")
    void testNegativesPending() {
        int[] arr = {3, -1, 2};
        // option 1 (recommended): throw IllegalArgumentException in radixSort if detect negative.
        assertThrows(IllegalArgumentException.class, () -> RadixSort.radixSort(arr));
    }
}