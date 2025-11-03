package sorting;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CountingSortTest {

    @Test
    void basicUnsortedArray() {
        int[] arr = {4, 2, 2, 8, 3, 3, 1};
        int[] expected = {1, 2, 2, 3, 3, 4, 8};
        assertArrayEquals(expected, CountingSort.countingSort(arr));
    }

    @Test
    void emptyArrayReturnsEmpty() {
        int[] arr = {};
        int[] expected = {};
        assertArrayEquals(expected, CountingSort.countingSort(arr));
    }

    @Test
    void alreadySortedArrayRemainsTheSame() {
        int[] arr = {1, 2, 3, 4, 5};
        int[] expected = {1, 2, 3, 4, 5};
        assertArrayEquals(expected, CountingSort.countingSort(arr));
    }

    @Test
    void reverseSortedArrayGetsSorted() {
        int[] arr = {5, 4, 3, 2, 1};
        int[] expected = {1, 2, 3, 4, 5};
        assertArrayEquals(expected, CountingSort.countingSort(arr));
    }

    @Test
    void arrayWithDuplicates() {
        int[] arr = {5, 5, 5, 2, 2, 9, 9, 1};
        int[] expected = {1, 2, 2, 5, 5, 5, 9, 9};
        assertArrayEquals(expected, CountingSort.countingSort(arr));
    }

    @Test
    void arrayAllEqualValues() {
        int[] arr = {7, 7, 7, 7};
        int[] expected = {7, 7, 7, 7};
        assertArrayEquals(expected, CountingSort.countingSort(arr));
    }

    @Test
    void arrayWithZeroIncluded() {
        int[] arr = {0, 5, 0, 3, 2, 2};
        int[] expected = {0, 0, 2, 2, 3, 5};
        assertArrayEquals(expected, CountingSort.countingSort(arr));
    }

    @Test
    void largeValuesWithinRange() {
        int[] arr = {100, 1, 50, 50, 100, 0};
        int[] expected = {0, 1, 50, 50, 100, 100};
        assertArrayEquals(expected, CountingSort.countingSort(arr));
    }

    @Test
    void singleElementArray() {
        int[] arr = {42};
        int[] expected = {42};
        assertArrayEquals(expected, CountingSort.countingSort(arr));
    }

    @Test
    void inputArrayIsNotModified() {
        int[] arr = {4, 1, 4, 3};
        int[] copy = arr.clone();
        CountingSort.countingSort(arr);
        // Ensure the original input is not modified (function is pure)
        assertArrayEquals(copy, arr);
    }
}