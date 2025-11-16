package data_structures.linkedlist.doubly_linked_list;

import java.util.NoSuchElementException;

public class DoublyLinkedListScratch<T> {

    public static class Node<T> {
        T value;
        Node<T> prev;
        Node<T> next;

        public Node(T value) {
            this.value = value;
        }

        public T getValue() {
            return value;
        }

        public Node<T> getPrev() {
            return prev;
        }

        public Node<T> getNext() {
            return next;
        }

        @Override
        public String toString() {
            return "Node(" + String.valueOf(value) + ")";
        }
    }

    private Node<T> head;
    private Node<T> tail;
    private int sizeValue;

    public DoublyLinkedListScratch() {
        this.head = null;
        this.tail = null;
        this.sizeValue = 0;
    }

    public boolean isEmpty() {
        return sizeValue == 0;
    }

    public int size() {
        return sizeValue;
    }

    private Node<T> makeNode(T value) {
        return new Node<>(value);
    }

    public Node<T> getHead() {
        return head;
    }

    public Node<T> getTail() {
        return tail;
    }

    
    public Node<T> pushFront(T value) {
        Node<T> n = makeNode(value);

        n.next = head;

        if (head != null) {
            head.prev = n;
        } else {
            tail = n;
        }

        head = n;
        sizeValue++;
        return n;
    }

    public Node<T> pushBack(T value) {
        Node<T> n = makeNode(value);

        if (tail == null) {
            head = tail = n;
        } else {
            n.prev = tail;
            tail.next = n;
            tail = n;
        }

        sizeValue++;
        return n;
    }

    public Node<T> insertAfter(Node<T> node, T value) {
        if (node == null) {
            throw new IllegalArgumentException("insertAfter: node cannot be null");
        }

        if (node == tail) {
            return pushBack(value);
        }

        Node<T> n = makeNode(value);
        Node<T> successor = node.next;

        n.prev = node;
        n.next = successor;

        node.next = n;
        if (successor != null) {
            successor.prev = n;
        }

        sizeValue++;
        return n;
    }

    public Node<T> insertBefore(Node<T> node, T value) {
        if (node == null) {
            throw new IllegalArgumentException("insertBefore: node cannot be null");
        }

        if (node == head) {
            return pushFront(value);
        }

        Node<T> n = makeNode(value);
        Node<T> predecessor = node.prev;

        n.next = node;
        n.prev = predecessor;

        if (predecessor != null) {
            predecessor.next = n;
        }
        node.prev = n;

        sizeValue++;
        return n;
    }

    public T popFront() {
        if (isEmpty()) {
            throw new NoSuchElementException("popFront from empty list");
        }

        Node<T> node = head;
        T value = node.value;

        if (head == tail) {
            head = tail = null;
        } else {
            head = head.next;
            head.prev = null;
        }

        sizeValue--;
        return value;
    }

    public T popBack() {
        if (isEmpty()) {
            throw new NoSuchElementException("popBack from empty list");
        }

        Node<T> node = tail;
        T value = node.value;

        if (head == tail) {
            head = tail = null;
        } else {
            tail = tail.prev;
            tail.next = null;
        }

        sizeValue--;
        return value;
    }

    public T remove(Node<T> node) {
        if (node == null) {
            throw new IllegalArgumentException("remove: node cannot be null");
        }

        if (isEmpty()) {
            throw new NoSuchElementException("remove from empty list");
        }

        if (node == head && node == tail) {
            head = tail = null;
        }
        else if (node == head) {
            head = node.next;
            head.prev = null;
        }
        else if (node == tail) {
            tail = node.prev;
            tail.next = null;
        }
        else {
            Node<T> prevNode = node.prev;
            Node<T> nextNode = node.next;
            prevNode.next = nextNode;
            nextNode.prev = prevNode;
        }

        node.prev = null;
        node.next = null;

        sizeValue--;
        return node.value;
    }

    public Node<T> find(T value) {
        Node<T> current = head;
        while (current != null) {
            if ((current.value == null && value == null) ||
                (current.value != null && current.value.equals(value))) {
                return current;
            }
            current = current.next;
        }
        return null;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("DoublyLinkedListScratch[");
        Node<T> current = head;
        while (current != null) {
            sb.append(String.valueOf(current.value));
            if (current.next != null) {
                sb.append(", ");
            }
            current = current.next;
        }
        sb.append("]");
        return sb.toString();
    }
}
