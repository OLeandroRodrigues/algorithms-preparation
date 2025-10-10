package heap.generic;

import org.junit.jupiter.api.Test;
import java.util.NoSuchElementException;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Unit tests for generic MaxHeap<T extends Comparable<T>>.
 */
class MaxHeapGenericTest {

    @Test
    void insertsAndPeeksMax() {
        MaxHeap<Integer> heap = new MaxHeap<>();
        heap.insert(10);
        heap.insert(50);
        heap.insert(30);

        assertEquals(50, heap.peek(), "Peek should return the maximum element");
        assertEquals(3, heap.size(), "Heap size should reflect number of insertions");
    }

    @Test
    void popsInDescendingOrder() {
        MaxHeap<Integer> heap = new MaxHeap<>();
        heap.insert(10);
        heap.insert(20);
        heap.insert(5);

        assertEquals(20, heap.pop());
        assertEquals(10, heap.pop());
        assertEquals(5, heap.pop());
        assertEquals(0, heap.size());
    }

    @Test
    void handlesEmptyHeap() {
        MaxHeap<Integer> heap = new MaxHeap<>();
        assertThrows(NoSuchElementException.class, heap::peek);
        assertThrows(NoSuchElementException.class, heap::pop);
    }

    @Test
    void singleElement() {
        MaxHeap<Integer> heap = new MaxHeap<>();
        heap.insert(42);
        assertEquals(42, heap.peek());
        assertEquals(42, heap.pop());
        assertEquals(0, heap.size());
    }

    @Test
    void mixedInsertAndPop() {
        MaxHeap<Integer> heap = new MaxHeap<>();
        heap.insert(5);
        heap.insert(15);
        assertEquals(15, heap.pop());

        heap.insert(20);
        heap.insert(1);
        assertEquals(20, heap.pop());
        assertEquals(5, heap.pop());
        assertEquals(1, heap.pop());
    }

    @Test
    void worksWithStrings() {
        MaxHeap<String> heap = new MaxHeap<>();
        heap.insert("apple");
        heap.insert("banana");
        heap.insert("pear");

        assertEquals("pear", heap.peek(), "Lexicographically largest string should be on top");
        assertEquals("pear", heap.pop());
        assertEquals("banana", heap.pop());
        assertEquals("apple", heap.pop());
    }

    @Test
    void worksWithCustomComparableType() {
        class Job implements Comparable<Job> {
            final String name;
            final int priority;
            Job(String name, int priority) {
                this.name = name;
                this.priority = priority;
            }

            @Override
            public int compareTo(Job other) {
                return Integer.compare(this.priority, other.priority);
            }

            @Override
            public String toString() {
                return name + "(" + priority + ")";
            }
        }

        MaxHeap<Job> heap = new MaxHeap<>();
        heap.insert(new Job("low", 1));
        heap.insert(new Job("mid", 5));
        heap.insert(new Job("high", 10));

        assertEquals("high", heap.peek().name);
        assertEquals("high", heap.pop().name);
        assertEquals("mid", heap.pop().name);
        assertEquals("low", heap.pop().name);
        assertEquals(0, heap.size());
    }

    @Test
    void heapMaintainsPropertyAfterMultipleOps() {
        MaxHeap<Integer> heap = new MaxHeap<>();
        for (int i = 0; i < 100; i++) heap.insert(i);
        for (int i = 99; i >= 0; i--) {
            assertEquals(i, heap.pop(), "Heap property must hold at step " + i);
        }
        assertTrue(heap.size() == 0);
    }
}