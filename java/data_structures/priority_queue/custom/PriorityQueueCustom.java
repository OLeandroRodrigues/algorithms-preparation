package priority_queue.custom;

import heap.generic.*;
import java.util.concurrent.atomic.AtomicLong;

/**
 * Priority Queue implementation using the existing MaxHeap.
 *
 * <p>Each element is stored as a PriorityItem (priority, -order, value) to ensure:
 * <ul>
 *   <li>Higher priority values are served first (max-priority behavior)</li>
 *   <li>FIFO stability between elements with the same priority (via negative order)</li>
 * </ul>
 *
 * <p>Time Complexity:
 * <ul>
 *   <li>push(): O(log n)</li>
 *   <li>pop():  O(log n)</li>
 *   <li>peek(): O(1)</li>
 *   <li>isEmpty(), size(): O(1)</li>
 * </ul>
 */
public class PriorityQueueCustom<T> {
    private final MaxHeap<PriorityItem<T>> heap;
    private final AtomicLong counter; 

    public PriorityQueueCustom() {
        this.heap = new MaxHeap<>();
        this.counter = new AtomicLong(0);
    }

    public void push(T value, int priority) {
        long order = counter.getAndIncrement();
        // Negative order ensures FIFO among elements with equal priority
        heap.insert(new PriorityItem<>(priority, -order, value));
    }

    public T pop() {
        if (isEmpty()) {
            throw new IllegalStateException("pop from an empty priority queue");
        }
        PriorityItem<T> item = heap.pop();
        return item.getValue();
    }

    public T peek() {
        if (isEmpty()) {
            throw new IllegalStateException("peek from an empty priority queue");
        }
        return heap.peek().getValue();
    }

    public boolean isEmpty() {
        return size() == 0;
    }

    public int size() {
        return heap.size();
    }

    private static class PriorityItem<T> implements Comparable<PriorityItem<T>> {
        private final int priority;
        private final long negOrder;
        private final T value;

        public PriorityItem(int priority, long negOrder, T value) {
            this.priority = priority;
            this.negOrder = negOrder;
            this.value = value;
        }

        public T getValue() {
            return value;
        }

        @Override
        public int compareTo(PriorityItem<T> other) {
            // Higher priority first
            if (this.priority != other.priority) {
                return Integer.compare(this.priority, other.priority);
            }
            // For equal priority, the higher negOrder (smaller insertion order) comes first
            return Long.compare(this.negOrder, other.negOrder);
        }

        @Override
        public String toString() {
            return String.format("(%d, %d, %s)", priority, negOrder, value);
        }
    }
}