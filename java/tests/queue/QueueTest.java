package data_structures.queue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.NoSuchElementException;

import static org.junit.jupiter.api.Assertions.*;

class QueueTest {

    private Queue<Integer> q;

    @BeforeEach
    void setUp() {
        q = new Queue<>();
    }

    @Test
    void enqueueDequeueOrder() {
        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        assertEquals(1, q.dequeue());
        assertEquals(2, q.dequeue());
        assertEquals(3, q.dequeue());
        assertTrue(q.isEmpty());
    }

    @Test
    void peekDoesNotRemove() {
        q.enqueue(10);
        q.enqueue(20);
        assertEquals(10, q.peek());
        assertEquals(2, q.size());
        assertEquals(10, q.dequeue());
        assertEquals(20, q.peek());
        assertEquals(1, q.size());
    }

    @Test
    void isEmptyAndSize() {
        assertTrue(q.isEmpty());
        assertEquals(0, q.size());
        q.enqueue(99);
        assertFalse(q.isEmpty());
        assertEquals(1, q.size());
    }

    @Test
    void dequeueEmptyThrows() {
        assertThrows(NoSuchElementException.class, () -> q.dequeue());
    }

    @Test
    void peekEmptyThrows() {
        assertThrows(NoSuchElementException.class, () -> q.peek());
    }
}
