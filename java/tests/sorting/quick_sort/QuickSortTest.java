package sorting;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class QuickSortTest {

    @Test
    void sortsReverse() {
        int[] arr = {9, 8, 7, 6, 5, 4, 3, 2, 1};
        int[] sorted = QuickSort.quickSort(arr);
        assertArrayEquals(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9}, sorted);
    }

    @Test
    void handlesEmptyAndSingle() {
        int[] empty = {};
        int[] sortedEmpty = QuickSort.quickSort(empty);
        assertArrayEquals(new int[]{}, sortedEmpty);

        int[] one = {42};
        int[] sortedOne = QuickSort.quickSort(one);
        assertArrayEquals(new int[]{42}, sortedOne);
    }

    @Test
    void alreadySorted() {
        int[] arr = {1, 2, 3, 4};
        int[] sorted = QuickSort.quickSort(arr);
        assertArrayEquals(new int[]{1, 2, 3, 4}, sorted);
    }

    @Test
    void sortsUnorderedList() {
        int[] arr = {3, 1, 4, 2};
        int[] sorted = QuickSort.quickSort(arr);
        assertArrayEquals(new int[]{1, 2, 3, 4}, sorted);
    }

    @Test
    void handlesDuplicates() {
        int[] arr = {4, 2, 2, 3, 1};
        int[] sorted = QuickSort.quickSort(arr);
        assertArrayEquals(new int[]{1, 2, 2, 3, 4}, sorted);
    }

    @Test
    void handlesNegativeNumbers() {
        int[] arr = {3, -1, -5, 2, 0};
        int[] sorted = QuickSort.quickSort(arr);
        assertArrayEquals(new int[]{-5, -1, 0, 2, 3}, sorted);
    }

    @Test
    void handlesAllEqualElements() {
        int[] arr = {7, 7, 7, 7};
        int[] sorted = QuickSort.quickSort(arr);
        assertArrayEquals(new int[]{7, 7, 7, 7}, sorted);
    }

    @Test
    void sortsLargeList() {
        int[] arr = {10, 3, 7, 2, 9, 1, 5, 8, 6, 4};
        int[] sorted = QuickSort.quickSort(arr);
        assertArrayEquals(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, sorted);
    }

    @Test
    void handlesMixedSignsAndDuplicates() {
        int[] arr = {0, -1, 5, -1, 3, 0, 2};
        int[] sorted = QuickSort.quickSort(arr);
        assertArrayEquals(new int[]{-1, -1, 0, 0, 2, 3, 5}, sorted);
    }
}
