package heap;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.util.NoSuchElementException;

class MinHeapTest {

    @Test
    void insertsAndPeeksMin() {
        MinHeap heap = new MinHeap();
        heap.insert(10);
        heap.insert(50);
        heap.insert(5);

        assertEquals(3, heap.size());
        assertEquals(5, heap.peek(), "Peek should return the minimum element");
    }

    @Test
    void popsInAscendingOrder() {
        MinHeap heap = new MinHeap();
        heap.insert(10);
        heap.insert(20);
        heap.insert(5);

        assertEquals(5, heap.pop());
        assertEquals(10, heap.pop());
        assertEquals(20, heap.pop());
        assertEquals(0, heap.size());
    }

    @Test
    void handlesEmptyHeap() {
        MinHeap heap = new MinHeap();
        assertThrows(NoSuchElementException.class, heap::peek);
        assertThrows(NoSuchElementException.class, heap::pop);
    }

    @Test
    void singleElement() {
        MinHeap heap = new MinHeap();
        heap.insert(42);

        assertEquals(42, heap.peek());
        assertEquals(42, heap.pop());
        assertEquals(0, heap.size());
    }

    @Test
    void mixedInsertAndPop() {
        MinHeap heap = new MinHeap();
        heap.insert(30);
        heap.insert(10);
        heap.insert(20);

        assertEquals(10, heap.pop());
        heap.insert(5);
        heap.insert(40);

        assertEquals(5, heap.pop());
        assertEquals(20, heap.pop());
        assertEquals(30, heap.pop());
        assertEquals(40, heap.pop());
        assertEquals(0, heap.size());
    }

    @Test
    void worksWithDuplicates() {
        MinHeap heap = new MinHeap();
        heap.insert(5);
        heap.insert(1);
        heap.insert(5);
        heap.insert(1);

        assertEquals(1, heap.pop());
        assertEquals(1, heap.pop());
        assertEquals(5, heap.pop());
        assertEquals(5, heap.pop());
        assertEquals(0, heap.size());
    }

    @Test
    void worksWithNegativeNumbers() {
        MinHeap heap = new MinHeap();
        heap.insert(0);
        heap.insert(-10);
        heap.insert(5);
        heap.insert(-3);
        heap.insert(2);

        assertEquals(-10, heap.pop());
        assertEquals(-3, heap.pop());
        assertEquals(0, heap.pop());
        assertEquals(2, heap.pop());
        assertEquals(5, heap.pop());
        assertEquals(0, heap.size());
    }
}