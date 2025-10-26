package selection;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class QuickSelectTest {

    @Test
    void findsKthSmallestBasic() {
        int[] arr = {7, 10, 4, 3, 20, 15};
        int result = QuickSelect.quickSelect(arr, 0, arr.length - 1, 3);
        assertEquals(7, result, "The 3rd smallest should be 7");
    }

    @Test
    void findsMinimumAndMaximum() {
        int[] arr = {8, 3, 5, 12, 1, 9};
        int min = QuickSelect.quickSelect(arr, 0, arr.length - 1, 1);
        int max = QuickSelect.quickSelect(arr, 0, arr.length - 1, arr.length);
        assertEquals(1, min, "1st smallest should be minimum");
        assertEquals(12, max, "n-th smallest should be maximum");
    }

    @Test
    void handlesDuplicates() {
        int[] arr = {4, 2, 2, 3, 1};
        int result = QuickSelect.quickSelect(arr, 0, arr.length - 1, 3);
        assertEquals(2, result, "3rd smallest should be 2 when duplicates exist");
    }

    @Test
    void handlesNegativeNumbers() {
        int[] arr = {3, -1, -5, 2, 0};
        int result = QuickSelect.quickSelect(arr, 0, arr.length - 1, 2);
        assertEquals(-1, result, "2nd smallest should be -1");
    }

    @Test
    void handlesAllEqualElements() {
        int[] arr = {7, 7, 7, 7};
        int result = QuickSelect.quickSelect(arr, 0, arr.length - 1, 2);
        assertEquals(7, result, "All elements are equal, any k-th smallest should be 7");
    }

    @Test
    void throwsIfKOutOfRange() {
        int[] arr = {1, 2, 3, 4, 5};
        assertThrows(IndexOutOfBoundsException.class, () -> 
            QuickSelect.quickSelect(arr, 0, arr.length - 1, 0),
            "k = 0 should raise IndexOutOfBoundsException"
        );
        assertThrows(IndexOutOfBoundsException.class, () -> 
            QuickSelect.quickSelect(arr, 0, arr.length - 1, 6),
            "k > n should raise IndexOutOfBoundsException"
        );
    }

    @Test
    void singleElementArray() {
        int[] arr = {42};
        int result = QuickSelect.quickSelect(arr, 0, 0, 1);
        assertEquals(42, result, "Single element array should return that element");
    }

    @Test
    void worksWithReverseOrderedArray() {
        int[] arr = {9, 8, 7, 6, 5};
        int result = QuickSelect.quickSelect(arr, 0, arr.length - 1, 2);
        assertEquals(6, result, "2nd smallest in descending array should be 6");
    }

    @Test
    void worksWithAlreadySortedArray() {
        int[] arr = {1, 2, 3, 4, 5};
        int result = QuickSelect.quickSelect(arr, 0, arr.length - 1, 4);
        assertEquals(4, result, "4th smallest in sorted array should be 4");
    }

    @Test
    void handlesLargeList() {
        int[] arr = {10, 3, 7, 2, 9, 1, 5, 8, 6, 4};
        int result = QuickSelect.quickSelect(arr, 0, arr.length - 1, 5);
        assertEquals(5, result, "5th smallest in list of 10 should be 5");
    }
}