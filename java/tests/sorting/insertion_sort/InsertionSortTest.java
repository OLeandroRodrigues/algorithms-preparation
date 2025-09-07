package sorting;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class InsertionSortTest {
    @Test void sortsReverse() {
        int[] arr = {9,8,7,6,5,4,3,2,1};
        InsertionSort.sort(arr);
        assertArrayEquals(new int[]{1,2,3,4,5,6,7,8,9}, arr);
    }
    @Test void handlesEmptyAndSingle() {
        int[] empty = {};
        InsertionSort.sort(empty);
        assertArrayEquals(new int[]{}, empty);

        int[] one = {42};
        InsertionSort.sort(one);
        assertArrayEquals(new int[]{42}, one);
    }
    @Test void alreadySorted() {
        int[] arr = {1,2,3,4};
        InsertionSort.sort(arr);
        assertArrayEquals(new int[]{1,2,3,4}, arr);
    }
}