package heap.generic;

import java.util.*; 

public class MaxHeap<T extends Comparable<T>> {

	private final List<T> data = new ArrayList<>();
	
	
	// --- Public API ---
    public void insert(T value) {
        data.add(value);
        heapifyUp(data.size() - 1);
    }

    public T pop() {
        if (data.isEmpty()) throw new NoSuchElementException("Heap is empty");
        T root = data.get(0);
        int lastIdx = data.size() - 1;

        // Move last to root, remove tail, then restore heap property.
        swap(0, lastIdx);
        data.remove(lastIdx);
        if (!data.isEmpty()) heapifyDown(0);

        return root;
    }

    public T peek() {
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
        // Bubble up while current > parent.
        while (i > 0) {
            int p = parent(i);
            if (data.get(i).compareTo(data.get(p)) <= 0) break;
            swap(i, p);
            i = p;
        }
    }

    private void heapifyDown(int i) {
        // Sift down while there is at least a left child.
        int n = data.size();
        while (left(i) < n) {
            int l = left(i), r = right(i);
            int largest = i;

            if (data.get(l).compareTo(data.get(largest)) > 0) largest = l;
            if (r < n && data.get(r).compareTo(data.get(largest)) > 0) largest = r;

            if (largest == i) break;
            swap(i, largest);
            i = largest;
        }
    }

    private void swap(int i, int j) {
        T tmp = data.get(i);
        data.set(i, data.get(j));
        data.set(j, tmp);
    }
}
