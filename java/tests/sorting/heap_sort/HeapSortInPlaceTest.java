package sorting;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.Arrays;

public class HeapSortInPlaceTest {

    @Test
    public void testAlreadySortedArray() {
        int[] arr = {1, 2, 3, 4, 5};
        int[] expected = {1, 2, 3, 4, 5};
        HeapSortInPlace.heapSort(arr);
        assertArrayEquals(expected, arr);
    }

    @Test
    public void testReverseSortedArray() {
        int[] arr = {9, 7, 5, 3, 1};
        int[] expected = {1, 3, 5, 7, 9};
        HeapSortInPlace.heapSort(arr);
        assertArrayEquals(expected, arr);
    }

    @Test
    public void testUnsortedArray() {
        int[] arr = {7, 51, 4, 10, 15, 30, 50};
        int[] expected = {4, 7, 10, 15, 30, 50, 51};
        HeapSortInPlace.heapSort(arr);
        assertArrayEquals(expected, arr);
    }

    @Test
    public void testArrayWithDuplicates() {
        int[] arr = {5, 1, 5, 3, 1, 2};
        int[] expected = {1, 1, 2, 3, 5, 5};
        HeapSortInPlace.heapSort(arr);
        assertArrayEquals(expected, arr);
    }

    @Test
    public void testSingleElementArray() {
        int[] arr = {42};
        int[] expected = {42};
        HeapSortInPlace.heapSort(arr);
        assertArrayEquals(expected, arr);
    }

    @Test
    public void testEmptyArray() {
        int[] arr = {};
        int[] expected = {};
        HeapSortInPlace.heapSort(arr);
        assertArrayEquals(expected, arr);
    }
}