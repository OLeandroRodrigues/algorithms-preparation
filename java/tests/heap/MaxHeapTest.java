package data_structures.heap;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class MaxHeapTest {

    @Test void insertsAndPeeksMax() {
        MaxHeap heap = new MaxHeap();
        heap.insert(10);
        heap.insert(50);
        heap.insert(30);

        assertEquals(50, heap.peek(), "Peek should return the maximum element");
        assertEquals(3, heap.size(), "Heap size should reflect number of insertions");
    }

    @Test void popsInDescendingOrder() {
        MaxHeap heap = new MaxHeap();
        heap.insert(10);
        heap.insert(20);
        heap.insert(5);

        assertEquals(20, heap.pop());
        assertEquals(10, heap.pop());
        assertEquals(5, heap.pop());
        assertEquals(0, heap.size());
    }

    @Test void handlesEmptyHeap() {
        MaxHeap heap = new MaxHeap();
        assertThrows(java.util.NoSuchElementException.class, heap::peek);
        assertThrows(java.util.NoSuchElementException.class, heap::pop);
    }

    @Test void singleElement() {
        MaxHeap heap = new MaxHeap();
        heap.insert(42);
        assertEquals(42, heap.peek());
        assertEquals(42, heap.pop());
        assertEquals(0, heap.size());
    }

    @Test void mixedInsertAndPop() {
        MaxHeap heap = new MaxHeap();
        heap.insert(5);
        heap.insert(15);
        assertEquals(15, heap.pop());

        heap.insert(20);
        heap.insert(1);
        assertEquals(20, heap.pop());
        assertEquals(5, heap.pop());
        assertEquals(1, heap.pop());
    }
}