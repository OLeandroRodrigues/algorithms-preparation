package priority_queue.custom;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Unit tests for PriorityQueueCustom<T>.
 *
 * Assumes heap.generic.MaxHeap<T> is available and PriorityQueueCustom<T>
 * delegates to it correctly.
 */
class PriorityQueueCustomTest {

    @Test
    @DisplayName("Max-priority order: higher priority comes out first")
    void testMaxPriorityOrder() {
        PriorityQueueCustom<String> pq = new PriorityQueueCustom<>();
        pq.push("low", 1);
        pq.push("mid", 5);
        pq.push("high", 9);

        assertEquals(3, pq.size());
        assertEquals("high", pq.peek());
        assertEquals("high", pq.pop());
        assertEquals("mid", pq.pop());
        assertEquals("low", pq.pop());
        assertTrue(pq.isEmpty());
    }

    @Test
    @DisplayName("Stability among equal priorities (FIFO within same priority)")
    void testStabilityEqualPriorities() {
        PriorityQueueCustom<String> pq = new PriorityQueueCustom<>();
        pq.push("A", 10); // first with priority 10
        pq.push("B", 10); // second with priority 10
        pq.push("C", 10); // third with priority 10

        assertEquals("A", pq.pop());
        assertEquals("B", pq.pop());
        assertEquals("C", pq.pop());
        assertTrue(pq.isEmpty());
    }

    @Test
    @DisplayName("Peek returns but does not remove the highest-priority element")
    void testPeekDoesNotRemove() {
        PriorityQueueCustom<String> pq = new PriorityQueueCustom<>();
        pq.push("x", 2);
        pq.push("y", 7);
        pq.push("z", 5);

        assertEquals(3, pq.size());
        assertEquals("y", pq.peek()); // highest priority
        assertEquals(3, pq.size());   // still there
        assertEquals("y", pq.pop());
        assertEquals("z", pq.pop());
        assertEquals("x", pq.pop());
    }

    @Test
    @DisplayName("Size and isEmpty reflect current state")
    void testSizeAndIsEmpty() {
        PriorityQueueCustom<String> pq = new PriorityQueueCustom<>();
        assertTrue(pq.isEmpty());
        assertEquals(0, pq.size());

        pq.push("a", 1);
        pq.push("b", 2);

        assertFalse(pq.isEmpty());
        assertEquals(2, pq.size());

        pq.pop();
        assertEquals(1, pq.size());

        pq.pop();
        assertTrue(pq.isEmpty());
        assertEquals(0, pq.size());
    }

    @Test
    @DisplayName("Pop on empty queue throws IllegalStateException")
    void testPopEmptyThrows() {
        PriorityQueueCustom<Integer> pq = new PriorityQueueCustom<>();
        assertThrows(IllegalStateException.class, pq::pop);
    }

    @Test
    @DisplayName("Peek on empty queue throws IllegalStateException")
    void testPeekEmptyThrows() {
        PriorityQueueCustom<Integer> pq = new PriorityQueueCustom<>();
        assertThrows(IllegalStateException.class, pq::peek);
    }

    @Test
    @DisplayName("Works with custom value types (T does not need to be Comparable)")
    void testWithCustomValueType() {
        class Job {
            final String id;
            final String payload;
            Job(String id, String payload) { this.id = id; this.payload = payload; }
        }

        PriorityQueueCustom<Job> pq = new PriorityQueueCustom<>();
        pq.push(new Job("J1", "alpha"), 3);
        pq.push(new Job("J2", "beta"), 10);
        pq.push(new Job("J3", "gamma"), 10);

        // Highest priority first, FIFO between ties
        assertEquals("J2", pq.pop().id);
        assertEquals("J3", pq.pop().id);
        assertEquals("J1", pq.pop().id);
        assertTrue(pq.isEmpty());
    }

    @Test
    @DisplayName("Mixed priorities and ties are handled correctly")
    void testMixedEqualAndDistinctPriorities() {
        PriorityQueueCustom<String> pq = new PriorityQueueCustom<>();
        pq.push("A1", 10);
        pq.push("B",   5);
        pq.push("A2", 10);
        pq.push("C",   7);
        pq.push("A3", 10);

        assertEquals("A1", pq.pop());
        assertEquals("A2", pq.pop());
        assertEquals("A3", pq.pop());
        assertEquals("C",  pq.pop());
        assertEquals("B",  pq.pop());
        assertTrue(pq.isEmpty());
    }
}