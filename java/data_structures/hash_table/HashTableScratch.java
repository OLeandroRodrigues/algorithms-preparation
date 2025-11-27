package data_structures.hash_table;

import java.util.Objects;

public class HashTableScratch<K, V> {

    private static class Node<K, V> {
        K key;
        V value;
        Node<K, V> next;

        Node(K key, V value, Node<K, V> next) {
            this.key  = key;
            this.value = value;
            this.next = next;
        }
    }

    private Node<K, V>[] buckets;
    private int capacity;
    private int size;
    private final double loadFactor;

    // -----------------------------
    //      Constructors
    // -----------------------------
    @SuppressWarnings("unchecked")
    public HashTableScratch(int capacity, double loadFactor) {
        if (capacity <= 0) {
            throw new IllegalArgumentException("capacity must be > 0");
        }
        if (loadFactor <= 0.0 || loadFactor >= 1.0) {
            throw new IllegalArgumentException("loadFactor must be in (0, 1)");
        }

        this.capacity = capacity;
        this.loadFactor = loadFactor;
        this.size = 0;
        this.buckets = (Node<K, V>[]) new Node[capacity];
    }

    public HashTableScratch() {
        this(8, 0.75);
    }

    // -----------------------------
    //      Internal helpers
    // -----------------------------
    private int hash(K key) {
        int h = Objects.hashCode(key);
        return h & 0x7FFFFFFF; // not negative
    }

    private int index(K key) {
        return hash(key) % capacity;
    }

    private boolean needsRehash() {
        return (double) size / capacity >= loadFactor;
    }

    @SuppressWarnings("unchecked")
    private void rehash() {
        Node<K, V>[] oldBuckets = buckets;
        capacity *= 2;
        buckets = (Node<K, V>[]) new Node[capacity];
        size = 0;

        for (Node<K, V> node : oldBuckets) {
            Node<K, V> current = node;
            while (current != null) {
                put(current.key, current.value);
                current = current.next;
            }
        }
    }

    // -----------------------------
    //       Public operations
    // -----------------------------
    public void put(K key, V value) {
        if (needsRehash()) {
            rehash();
        }

        int idx = index(key);
        Node<K, V> head = buckets[idx];

        Node<K, V> current = head;
        while (current != null) {
            if (Objects.equals(current.key, key)) {
                current.value = value; // update
                return;
            }
            current = current.next;
        }

        Node<K, V> newNode = new Node<>(key, value, head);
        buckets[idx] = newNode;
        size++;
    }

    public V get(K key) {
        int idx = index(key);
        Node<K, V> current = buckets[idx];

        while (current != null) {
            if (Objects.equals(current.key, key)) {
                return current.value;
            }
            current = current.next;
        }

        throw new IllegalStateException("Key not found: " + key);
    }

    public boolean remove(K key) {
        int idx = index(key);
        Node<K, V> current = buckets[idx];
        Node<K, V> prev = null;

        while (current != null) {
            if (Objects.equals(current.key, key)) {
                if (prev == null) {
                    buckets[idx] = current.next;
                } else {
                    prev.next = current.next;
                }
                size--;
                return true;
            }

            prev = current;
            current = current.next;
        }

        return false;
    }

    public boolean contains(K key) {
        int idx = index(key);
        Node<K, V> current = buckets[idx];

        while (current != null) {
            if (Objects.equals(current.key, key)) {
                return true;
            }
            current = current.next;
        }

        return false;
    }

    public int size() {
        return size;
    }

    public double currentLoadFactor() {
        return (double) size / capacity;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("{ ");
        boolean first = true;

        for (Node<K, V> bucket : buckets) {
            Node<K, V> current = bucket;
            while (current != null) {
                if (!first) {
                    sb.append(", ");
                }
                sb.append(current.key).append(": ").append(current.value);
                first = false;
                current = current.next;
            }
        }

        sb.append(" }");
        return sb.toString();
    }


    public static void main(String[] args) {
        HashTableScratch<String, Integer> table = new HashTableScratch<>();

        table.put("a", 1);
        table.put("b", 2);
        table.put("c", 3);

        System.out.println(table);
        System.out.println("a -> " + table.get("a"));
        System.out.println("contains b? " + table.contains("b"));

        table.remove("b");
        System.out.println("after remove(b): " + table);
        System.out.println("contains b? " + table.contains("b"));
        System.out.println("size = " + table.size());
        System.out.println("loadFactor = " + table.currentLoadFactor());
    }
}
