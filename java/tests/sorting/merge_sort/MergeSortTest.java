package sorting;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class MergeSortTest {

    @Test void sortsReverse() {
        int[] arr = {9,8,7,6,5,4,3,2,1};
        int[] sorted = MergeSort.mergeSort(arr);
        assertArrayEquals(new int[]{1,2,3,4,5,6,7,8,9}, sorted);
    }

    @Test void handlesEmptyAndSingle() {
        int[] empty = {};
        int[] sortedEmpty = MergeSort.mergeSort(empty);
        assertArrayEquals(new int[]{}, sortedEmpty);

        int[] one = {42};
        int[] sortedOne = MergeSort.mergeSort(one);
        assertArrayEquals(new int[]{42}, sortedOne);
    }

    @Test void alreadySorted() {
        int[] arr = {1,2,3,4};
        int[] sorted = MergeSort.mergeSort(arr);
        assertArrayEquals(new int[]{1,2,3,4}, sorted);
    }

}