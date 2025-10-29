package algorithms.sorting.quick_sort;

import algorithms.sorting.quick_sort.randomized.QuickSortRandomized;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class QuickSortRandomizedTest {

    @Test
    void sortsReverse() {
        int[] arr = {9, 8, 7, 6, 5, 4, 3, 2, 1};
        QuickSortRandomized.quickSort(arr, 0, arr.length - 1);
        assertArrayEquals(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9}, arr);
    }

    @Test
    void handlesEmptyAndSingle() {
        int[] empty = {};
        QuickSortRandomized.quickSort(empty, 0, empty.length - 1);
        assertArrayEquals(new int[]{}, empty);

        int[] one = {42};
        QuickSortRandomized.quickSort(one, 0, one.length - 1);
        assertArrayEquals(new int[]{42}, one);
    }

    @Test
    void alreadySorted() {
        int[] arr = {1, 2, 3, 4};
        QuickSortRandomized.quickSort(arr, 0, arr.length - 1);
        assertArrayEquals(new int[]{1, 2, 3, 4}, arr);
    }

    @Test
    void sortsUnorderedList() {
        int[] arr = {3, 1, 4, 2};
        QuickSortRandomized.quickSort(arr, 0, arr.length - 1);
        assertArrayEquals(new int[]{1, 2, 3, 4}, arr);
    }

    @Test
    void handlesDuplicates() {
        int[] arr = {4, 2, 2, 3, 1};
        QuickSortRandomized.quickSort(arr, 0, arr.length - 1);
        assertArrayEquals(new int[]{1, 2, 2, 3, 4}, arr);
    }

    @Test
    void handlesNegativeNumbers() {
        int[] arr = {3, -1, -5, 2, 0};
        QuickSortRandomized.quickSort(arr, 0, arr.length - 1);
        assertArrayEquals(new int[]{-5, -1, 0, 2, 3}, arr);
    }

    @Test
    void handlesAllEqualElements() {
        int[] arr = {7, 7, 7, 7};
        QuickSortRandomized.quickSort(arr, 0, arr.length - 1);
        assertArrayEquals(new int[]{7, 7, 7, 7}, arr);
    }

    @Test
    void sortsLargeList() {
        int[] arr = {10, 3, 7, 2, 9, 1, 5, 8, 6, 4};
        QuickSortRandomized.quickSort(arr, 0, arr.length - 1);
        assertArrayEquals(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, arr);
    }

    @Test
    void handlesMixedSignsAndDuplicates() {
        int[] arr = {0, -1, 5, -1, 3, 0, 2};
        QuickSortRandomized.quickSort(arr, 0, arr.length - 1);
        assertArrayEquals(new int[]{-1, -1, 0, 0, 2, 3, 5}, arr);
    }
}