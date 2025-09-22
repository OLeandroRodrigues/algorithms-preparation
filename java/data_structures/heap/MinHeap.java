package heap;

import java.util.*;

public class MinHeap {

    private final List<Integer> data = new ArrayList<>();

    // --- Public API ---
    public void insert(int value) {
        data.add(value);
        heapifyUp(data.size() - 1);
    }

    public int pop() {
        if (data.isEmpty()) throw new NoSuchElementException("Heap is empty");
        int root = data.get(0);
        int lastIdx = data.size() - 1;

        // Move last to root, remove tail, then restore heap property.
        swap(0, lastIdx);
        data.remove(lastIdx);
        if (!data.isEmpty()) heapifyDown(0);

        return root;
    }

    public int peek() {
        if (data.isEmpty()) throw new NoSuchElementException("Heap is empty");
        return data.get(0);
    }

    public int size() {
        return data.size();
    }

    // --- Internals ---
    private static int parent(int i) { return (i - 1) / 2; }
    private static int left(int i)   { return 2 * i + 1; }
    private static int right(int i)  { return 2 * i + 2; }

    private void heapifyUp(int i) {
        // Bubble up while current < parent (Min-Heap).
        while (i > 0) {
            int p = parent(i);
            if (data.get(i) >= data.get(p)) break;  // <-- correção: deve parar quando o filho não é menor que o pai
            swap(i, p);
            i = p;
        }
    }

    private void heapifyDown(int i) {
        // Sift down while there is at least a left child.
        int n = data.size();
        while (left(i) < n) {
            int smallest = i;
            int l = left(i), r = right(i);

            if (data.get(l) < data.get(smallest)) smallest = l;
            if (r < n && data.get(r) < data.get(smallest)) smallest = r;

            if (smallest == i) break;
            swap(i, smallest);
            i = smallest;
        }
    }

    private void swap(int i, int j) {
        int tmp = data.get(i);
        data.set(i, data.get(j));
        data.set(j, tmp);
    }
}