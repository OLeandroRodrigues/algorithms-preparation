package priority_queue.builtin;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PriorityQueueBuiltinTest {

    @Test
    @DisplayName("Max-priority mode: higher priorities come out first")
    void testMaxPriorityOrder() {
        PriorityQueueBuiltin<String> pq = new PriorityQueueBuiltin<>(false);
        pq.push("low", 1);
        pq.push("mid", 5);
        pq.push("high", 10);

        assertEquals(3, pq.size());
        assertEquals("high", pq.peek());
        assertEquals("high", pq.pop());
        assertEquals("mid", pq.pop());
        assertEquals("low", pq.pop());
        assertTrue(pq.isEmpty());
    }

    @Test
    @DisplayName("Min-priority mode: lower priorities come out first")
    void testMinPriorityOrder() {
        PriorityQueueBuiltin<String> pq = new PriorityQueueBuiltin<>(true);
        pq.push("low", 1);
        pq.push("mid", 5);
        pq.push("high", 10);

        assertEquals(3, pq.size());
        assertEquals("low", pq.peek());
        assertEquals("low", pq.pop());
        assertEquals("mid", pq.pop());
        assertEquals("high", pq.pop());
        assertTrue(pq.isEmpty());
    }

    @Test
    @DisplayName("Stability: elements with same priority come out in FIFO order")
    void testStabilityEqualPriorities() {
        PriorityQueueBuiltin<String> pq = new PriorityQueueBuiltin<>(false);
        pq.push("A", 10);
        pq.push("B", 10);
        pq.push("C", 10);

        assertEquals("A", pq.pop());
        assertEquals("B", pq.pop());
        assertEquals("C", pq.pop());
        assertTrue(pq.isEmpty());
    }

    @Test
    @DisplayName("Peek returns but does not remove the next element")
    void testPeekDoesNotRemove() {
        PriorityQueueBuiltin<String> pq = new PriorityQueueBuiltin<>(false);
        pq.push("x", 3);
        pq.push("y", 8);
        pq.push("z", 5);

        assertEquals(3, pq.size());
        assertEquals("y", pq.peek());
        assertEquals(3, pq.size());
        assertEquals("y", pq.pop());
        assertEquals("z", pq.pop());
        assertEquals("x", pq.pop());
    }

    @Test
    @DisplayName("Size and isEmpty reflect current state")
    void testSizeAndIsEmpty() {
        PriorityQueueBuiltin<String> pq = new PriorityQueueBuiltin<>(true);
        assertTrue(pq.isEmpty());
        assertEquals(0, pq.size());

        pq.push("A", 1);
        pq.push("B", 2);
        assertFalse(pq.isEmpty());
        assertEquals(2, pq.size());

        pq.pop();
        assertEquals(1, pq.size());
        pq.pop();
        assertTrue(pq.isEmpty());
    }

    @Test
    @DisplayName("Pop and peek on empty queue throw IllegalStateException")
    void testEmptyQueueThrows() {
        PriorityQueueBuiltin<Integer> pq = new PriorityQueueBuiltin<>();
        assertThrows(IllegalStateException.class, pq::pop);
        assertThrows(IllegalStateException.class, pq::peek);
    }

    @Test
    @DisplayName("Clear removes all elements and resets size")
    void testClear() {
        PriorityQueueBuiltin<String> pq = new PriorityQueueBuiltin<>(false);
        pq.push("A", 1);
        pq.push("B", 2);
        pq.push("C", 3);

        assertEquals(3, pq.size());
        pq.clear();
        assertTrue(pq.isEmpty());
        assertEquals(0, pq.size());
        assertThrows(IllegalStateException.class, pq::pop);
    }

    @Test
    @DisplayName("Works with custom object types")
    void testWithCustomObjects() {
        class Task {
            final String id;
            final int priority;
            Task(String id, int priority) { this.id = id; this.priority = priority; }
        }

        PriorityQueueBuiltin<Task> pq = new PriorityQueueBuiltin<>(false);
        pq.push(new Task("T1", 10), 10);
        pq.push(new Task("T2", 20), 20);
        pq.push(new Task("T3", 15), 15);

        assertEquals("T2", pq.pop().id);
        assertEquals("T3", pq.pop().id);
        assertEquals("T1", pq.pop().id);
        assertTrue(pq.isEmpty());
    }

    @Test
    @DisplayName("Mixed priorities and stability are preserved")
    void testMixedPrioritiesAndStability() {
        PriorityQueueBuiltin<String> pq = new PriorityQueueBuiltin<>(false);
        pq.push("A1", 10);
        pq.push("B", 5);
        pq.push("A2", 10);
        pq.push("C", 7);
        pq.push("A3", 10);

        assertEquals("A1", pq.pop());
        assertEquals("A2", pq.pop());
        assertEquals("A3", pq.pop());
        assertEquals("C", pq.pop());
        assertEquals("B", pq.pop());
        assertTrue(pq.isEmpty());
    }
}