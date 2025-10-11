package priority_queue.builtin;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.concurrent.atomic.AtomicLong;

/**
 * Priority Queue implemented with Java's built-in PriorityQueue.
 *
 * Features:
 * - Min or Max behavior (configurable via constructor).
 * - Stable among equal priorities (FIFO) using a monotonic counter.
 *
 * API:
 *  - push(value, priority) : O(log n)
 *  - pop()                 : O(log n)
 *  - peek()                : O(1)
 *  - size(), isEmpty()     : O(1)
 *  - clear()               : O(n)
 */
public class PriorityQueueBuiltin<T> {

    private static final class Node<T> {
        final int priority;
        final long order; 
        final T value;

        Node(int priority, long order, T value) {
            this.priority = priority;
            this.order = order;
            this.value = value;
        }
    }

    private final PriorityQueue<Node<T>> pq;
    private final AtomicLong counter = new AtomicLong(0);


    public PriorityQueueBuiltin() {
        this(true);
    }


    public PriorityQueueBuiltin(boolean isMin) {
        Comparator<Node<T>> cmp = (a, b) -> {
            if (a.priority != b.priority) {
                return isMin
                        ? Integer.compare(a.priority, b.priority)      // min: lower first
                        : Integer.compare(b.priority, a.priority);     // max: higher first
            }
            return Long.compare(a.order, b.order);
        };
        this.pq = new PriorityQueue<>(cmp);
    }

    public void push(T value, int priority) {
        long order = counter.getAndIncrement(); // tie-breaker for stability
        pq.add(new Node<>(priority, order, value));
    }

    public T pop() {
        Node<T> n = pq.poll();
        if (n == null) throw new IllegalStateException("pop from an empty priority queue");
        return n.value;
    }

    public T peek() {
        Node<T> n = pq.peek();
        if (n == null) throw new IllegalStateException("peek from an empty priority queue");
        return n.value;
    }

    /* Current number of elements. */
    public int size() {
        return pq.size();
    }

    /* True if the queue has no elements. */
    public boolean isEmpty() {
        return pq.isEmpty();
    }

    /* Remove all elements. */
    public void clear() {
        pq.clear();
    }
}