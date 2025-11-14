package data_structures.linkedlist;

public class SinglyLinkedListScratch {

    public static class Node {
        public Object value;
        public Node next;

        public Node(Object value) {
            this.value = value;
            this.next = null;
        }
    }

    private Node head;
    private Node tail;
    private int sizeValue;

    public SinglyLinkedListScratch() {
        this.head = null;
        this.tail = null;
        this.sizeValue = 0;
    }

    private Node makeNode(Object value) {
        return new Node(value);
    }

    public Node pushFront(Object value) {
        Node n = makeNode(value);
        n.next = head;
        head = n;

        if (tail == null) {
            tail = n;
        }

        sizeValue++;
        return n;
    }

    public Node pushBack(Object value) {
        Node n = makeNode(value);

        if (tail == null) {
            head = tail = n;
        } else {
            tail.next = n;
            tail = n;
        }

        sizeValue++;
        return n;
    }

    public Node insertAfter(Node node, Object value) {
        if (node == null) {
            throw new IllegalArgumentException("insert_after: node cannot be null");
        }

        Node n = makeNode(value);
        n.next = node.next;
        node.next = n;

        if (tail == node) {
            tail = n;
        }

        sizeValue++;
        return n;
    }

    public Object popFront() {
        if (head == null) {
            throw new RuntimeException("pop_front from empty list");
        }

        Object value = head.value;
        head = head.next;
        sizeValue--;

        if (head == null) {
            tail = null;
        }

        return value;
    }

    public Object removeAfter(Node node) {
        if (node == null || node.next == null) {
            throw new IllegalArgumentException("remove_after: nothing to remove");
        }

        Node toRemove = node.next;
        node.next = toRemove.next;

        if (tail == toRemove) {
            tail = node;
        }

        sizeValue--;
        return toRemove.value;
    }

    public Node find(Object value) {
        Node current = head;
        while (current != null) {
            if ((current.value == null && value == null) ||
                (current.value != null && current.value.equals(value))) {
                return current;
            }
            current = current.next;
        }
        return null;
    }

    public boolean isEmpty() {
        return sizeValue == 0;
    }

    public int size() {
        return sizeValue;
    }

    public Node getHead() {
        return head;
    }

    public Node getTail() {
        return tail;
    }
}