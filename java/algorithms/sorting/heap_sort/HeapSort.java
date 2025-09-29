package sorting;

import data_structures.heap.MaxHeap;  
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class HeapSort {
    /**
     * HeapSort implementation reusing the existing MaxHeap.
     * - sortAsc: returns ascending order
     * - sortDesc: returns descending order
     * Note: returns a NEW list (does not mutate the input).
     */

    public static List<Integer> sortDesc(List<Integer> arr) {
        // Sorts in descending order by reusing MaxHeap:
        // inserts all elements and repeatedly pops the max (largest -> smallest).
        MaxHeap heap = new MaxHeap();
        for (int item : arr) {
            heap.insert(item);
        }

        List<Integer> result = new ArrayList<>();
        while (heap.size() != 0) {
            result.add(heap.pop());
        }
        return result;
    }

    public static List<Integer> sortAsc(List<Integer> arr) {
        // Sorts in ascending order using the same MaxHeap:
        // obtains the descending list and then reverses it.
        List<Integer> desc = sortDesc(arr);
        Collections.reverse(desc);
        return desc;
    }

    // Demo
    public static void main(String[] args) {
        List<Integer> A = List.of(4, 5, 5, 10, 10, 8, 2, 100, 50, 30, 1);

        System.out.println("Asc : " + HeapSort.sortAsc(A));
        // [1, 2, 4, 5, 5, 8, 10, 10, 30, 50, 100]

        System.out.println("Desc: " + HeapSort.sortDesc(A));
        // [100, 50, 30, 10, 10, 8, 5, 5, 4, 2, 1]
    }
}