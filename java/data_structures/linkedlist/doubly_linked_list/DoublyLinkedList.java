package data_structures.linkedlist.doubly_linked_list;

import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.Objects;

/**
 * A simple, production-ready implementation of a doubly linked list.
 *
 * <p>This class is intentionally close in spirit to a minimal {@code Deque<T>}:
 * it supports adding/removing at both ends in O(1), iteration in forward
 * order, and a descending iterator.</p>
 *
 * <p>Not thread-safe.</p>
 */
public class DoublyLinkedList<T> implements Iterable<T> {

    /**
     * Internal node representation. Not exposed outside this class.
     */
    private static final class Node<E> {
        E item;
        Node<E> prev;
        Node<E> next;

        Node(Node<E> prev, E item, Node<E> next) {
            this.prev = prev;
            this.item = item;
            this.next = next;
        }
    }

    private Node<T> head;
    private Node<T> tail;
    private int size;

    /**
     * Creates an empty list.
     */
    public DoublyLinkedList() {
        // head, tail = null; size = 0;
    }

    /**
     * Creates a list populated with all elements from the given iterable,
     * in iteration order.
     */
    public DoublyLinkedList(Iterable<? extends T> elements) {
        this();
        Objects.requireNonNull(elements, "elements must not be null");
        for (T e : elements) {
            addLast(e);
        }
    }

    // ------------------------------------------------------------------
    // Basic properties / helpers
    // ------------------------------------------------------------------

    /**
     * Returns the number of elements in this list.
     */
    public int size() {
        return size;
    }

    /**
     * Returns {@code true} if this list contains no elements.
     */
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * Removes all elements from this list.
     */
    public void clear() {
        Node<T> current = head;
        while (current != null) {
            Node<T> next = current.next;
            current.prev = null;
            current.next = null;
            current.item = null;
            current = next;
        }
        head = tail = null;
        size = 0;
    }

    // ------------------------------------------------------------------
    // Core operations: add/remove/peek at both ends
    // ------------------------------------------------------------------

    /**
     * Inserts the specified element at the front of this list.
     */
    public void addFirst(T element) {
        Node<T> newNode = new Node<>(null, element, head);

        if (head == null) {
            // list was empty
            head = tail = newNode;
        } else {
            head.prev = newNode;
            head = newNode;
        }

        size++;
    }

    /**
     * Inserts the specified element at the end of this list.
     */
    public void addLast(T element) {
        Node<T> newNode = new Node<>(tail, element, null);

        if (tail == null) {
            // list was empty
            head = tail = newNode;
        } else {
            tail.next = newNode;
            tail = newNode;
        }

        size++;
    }

    /**
     * Returns, but does not remove, the first element of this list,
     * or {@code null} if the list is empty.
     */
    public T peekFirst() {
        return (head == null) ? null : head.item;
    }

    /**
     * Returns, but does not remove, the last element of this list,
     * or {@code null} if the list is empty.
     */
    public T peekLast() {
        return (tail == null) ? null : tail.item;
    }

    /**
     * Removes and returns the first element of this list.
     *
     * @throws NoSuchElementException if the list is empty
     */
    public T removeFirst() {
        if (head == null) {
            throw new NoSuchElementException("removeFirst from empty list");
        }

        Node<T> node = head;
        T value = node.item;

        if (head == tail) {
            // single element
            head = tail = null;
        } else {
            head = head.next;
            Objects.requireNonNull(head).prev = null;
        }

        // help GC
        node.next = null;
        node.item = null;
        size--;
        return value;
    }

    /**
     * Removes and returns the last element of this list.
     *
     * @throws NoSuchElementException if the list is empty
     */
    public T removeLast() {
        if (tail == null) {
            throw new NoSuchElementException("removeLast from empty list");
        }

        Node<T> node = tail;
        T value = node.item;

        if (head == tail) {
            head = tail = null;
        } else {
            tail = tail.prev;
            Objects.requireNonNull(tail).next = null;
        }

        // help GC
        node.prev = null;
        node.item = null;
        size--;
        return value;
    }

    // ------------------------------------------------------------------
    // Search / removal by value
    // ------------------------------------------------------------------

    /**
     * Returns {@code true} if this list contains at least one element
     * equal to {@code value}, using {@link Objects#equals(Object, Object)}.
     */
    public boolean contains(Object value) {
        return indexOfNode(value) != null;
    }

    /**
     * Removes the first occurrence of the specified element from this list,
     * if it is present.
     *
     * @return {@code true} if an element was removed, {@code false} otherwise
     */
    public boolean removeFirstOccurrence(Object value) {
        Node<T> node = indexOfNode(value);
        if (node == null) {
            return false;
        }
        unlink(node);
        return true;
    }

    /**
     * Internal search for a node whose item equals the given value.
     */
    private Node<T> indexOfNode(Object value) {
        for (Node<T> current = head; current != null; current = current.next) {
            if (Objects.equals(current.item, value)) {
                return current;
            }
        }
        return null;
    }

    /**
     * Unlinks the given node from the list, adjusting head/tail and size.
     * Assumes the node belongs to this list.
     */
    private void unlink(Node<T> node) {
        Node<T> prev = node.prev;
        Node<T> next = node.next;

        if (prev == null) {
            // node is head
            head = next;
        } else {
            prev.next = next;
        }

        if (next == null) {
            // node is tail
            tail = prev;
        } else {
            next.prev = prev;
        }

        node.prev = null;
        node.next = null;
        node.item = null;
        size--;
    }

    // ------------------------------------------------------------------
    // Iteration
    // ------------------------------------------------------------------

    /**
     * Returns an iterator over the elements in this list in proper sequence
     * (from first to last).
     */
    @Override
    public Iterator<T> iterator() {
        return new Iterator<T>() {
            private Node<T> current = head;
            private Node<T> lastReturned = null;

            @Override
            public boolean hasNext() {
                return current != null;
            }

            @Override
            public T next() {
                if (current == null) {
                    throw new NoSuchElementException();
                }
                lastReturned = current;
                current = current.next;
                return lastReturned.item;
            }

            @Override
            public void remove() {
                if (lastReturned == null) {
                    throw new IllegalStateException("next() has not been called or element already removed");
                }
                unlink(lastReturned);
                lastReturned = null;
            }
        };
    }

    /**
     * Returns an iterable that iterates the elements in reverse order
     * (from last to first).
     */
    public Iterable<T> descendingIterable() {
        return () -> new Iterator<T>() {
            private Node<T> current = tail;
            private Node<T> lastReturned = null;

            @Override
            public boolean hasNext() {
                return current != null;
            }

            @Override
            public T next() {
                if (current == null) {
                    throw new NoSuchElementException();
                }
                lastReturned = current;
                current = current.prev;
                return lastReturned.item;
            }

            @Override
            public void remove() {
                if (lastReturned == null) {
                    throw new IllegalStateException("next() has not been called or element already removed");
                }
                unlink(lastReturned);
                lastReturned = null;
            }
        };
    }

    // ------------------------------------------------------------------
    // toString / debug helpers
    // ------------------------------------------------------------------

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("DoublyLinkedList[");
        Node<T> current = head;
        while (current != null) {
            sb.append(String.valueOf(current.item));
            if (current.next != null) {
                sb.append(", ");
            }
            current = current.next;
        }
        sb.append(']');
        return sb.toString();
    }
}
