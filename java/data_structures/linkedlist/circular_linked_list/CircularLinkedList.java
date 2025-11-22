package data_structures.linkedlist.circular_linked_list;

public class CircularLinkedList<T> {

    public static class Node<T> {
        T value;
        Node<T> next;

        Node(T value) {
            this.value = value;
        }
    }

    public Node<T> tail;  // tail.next = head
    public int size;

    public CircularLinkedList() {
        this.tail = null;
        this.size = 0;
    }


    public boolean isEmpty() {
        return tail == null;
    }

    public int size() {
        return size;
    }

    // Insert at beginning (head)
    public void addFirst(T value) {
        Node<T> newNode = new Node<>(value);

        if (isEmpty()) {
            tail = newNode;
            newNode.next = newNode;   // circular: points to itself
        } else {
            newNode.next = tail.next; // current head
            tail.next = newNode;      // newNode becomes new head
        }

        size++;
    }

    // Insert at end (tail)
    public void addLast(T value) {
        addFirst(value);
        tail = tail.next; // move tail to the newly added node
    }

    // Remove first (head)
    public T removeFirst() {
        if (isEmpty()) {
            throw new IllegalStateException("removeFirst from empty list");
        }

        Node<T> head = tail.next;
        T value = head.value;

        // Only one node in the list
        if (tail == head) {
            tail = null;
        } else {
            tail.next = head.next; // bypass old head
        }

        size--;
        return value;
    }

    // Get first element
    public T getFirst() {
        if (isEmpty()) {
            throw new IllegalStateException("getFirst from empty list");
        }
        return tail.next.value; // head
    }

    // Get last element
    public T getLast() {
        if (isEmpty()) {
            throw new IllegalStateException("getLast from empty list");
        }
        return tail.value;
    }

    // Find value in the cycle
    public Node<T> find(T value) {
        if (isEmpty()) return null;

        Node<T> current = tail.next; // head

        while (true) {
            if ((current.value == null && value == null) ||
                (current.value != null && current.value.equals(value))) {
                return current;
            }

            current = current.next;

            if (current == tail.next) {
                break; // full cycle completed
            }
        }

        return null;
    }

    @Override
    public String toString() {
        if (isEmpty()) {
            return "CircularLinkedList([])";
        }

        StringBuilder sb = new StringBuilder("CircularLinkedList([");
        Node<T> current = tail.next; // head

        while (true) {
            sb.append(current.value);
            current = current.next;

            if (current == tail.next) {
                break;
            }
            sb.append(", ");
        }

        sb.append("])");
        return sb.toString();
    }
}
