package data_structures.linkedlist.circular_linked_list;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class CircularLinkedListTest {

    @Test
    void new_list_is_empty() {
        CircularLinkedList<Integer> cll = new CircularLinkedList<>();

        assertTrue(cll.isEmpty());
        assertEquals(0, cll.size());
        assertEquals("CircularLinkedList([])", cll.toString());
    }

    @Test
    void add_first_single_element() {
        CircularLinkedList<Integer> cll = new CircularLinkedList<>();

        cll.addFirst(10);

        assertFalse(cll.isEmpty());
        assertEquals(1, cll.size());
        assertEquals(10, cll.getFirst());
        assertEquals(10, cll.getLast());

        // circular property: tail.next is head and head is tail
        CircularLinkedList.Node<Integer> tail = cll.tail; // same package, accessible
        assertNotNull(tail);
        assertSame(tail, tail.next);
    }

    @Test
    void add_first_multiple_elements() {
        CircularLinkedList<Integer> cll = new CircularLinkedList<>();

        cll.addFirst(10);
        cll.addFirst(20);
        cll.addFirst(30);

        // list should be [30, 20, 10]
        assertEquals(3, cll.size());
        assertEquals(30, cll.getFirst());
        assertEquals(10, cll.getLast());
        assertEquals("CircularLinkedList([30, 20, 10])", cll.toString());
    }

    @Test
    void add_last_single_and_multiple() {
        CircularLinkedList<Integer> cll = new CircularLinkedList<>();

        cll.addLast(10);
        assertEquals(1, cll.size());
        assertEquals(10, cll.getFirst());
        assertEquals(10, cll.getLast());

        cll.addLast(20);
        cll.addLast(30);

        // list [10, 20, 30]
        assertEquals(3, cll.size());
        assertEquals(10, cll.getFirst());
        assertEquals(30, cll.getLast());
        assertEquals("CircularLinkedList([10, 20, 30])", cll.toString());
    }

    @Test
    void remove_first_single_element() {
        CircularLinkedList<Integer> cll = new CircularLinkedList<>();

        cll.addLast(42);
        assertEquals(1, cll.size());

        int removed = cll.removeFirst();
        assertEquals(42, removed);
        assertTrue(cll.isEmpty());
        assertEquals(0, cll.size());
        assertEquals("CircularLinkedList([])", cll.toString());
    }

    @Test
    void remove_first_multiple_elements() {
        CircularLinkedList<Integer> cll = new CircularLinkedList<>();

        cll.addLast(10);
        cll.addLast(20);
        cll.addLast(30);

        // [10, 20, 30]
        assertEquals(3, cll.size());

        int v1 = cll.removeFirst();
        assertEquals(10, v1);
        assertEquals(2, cll.size());
        assertEquals(20, cll.getFirst());
        assertEquals(30, cll.getLast());

        int v2 = cll.removeFirst();
        assertEquals(20, v2);
        assertEquals(1, cll.size());
        assertEquals(30, cll.getFirst());
        assertEquals(30, cll.getLast());

        int v3 = cll.removeFirst();
        assertEquals(30, v3);
        assertTrue(cll.isEmpty());
        assertEquals(0, cll.size());
    }

    @Test
    void remove_first_from_empty_throws() {
        CircularLinkedList<Integer> cll = new CircularLinkedList<>();

        assertThrows(IllegalStateException.class, cll::removeFirst);
    }

    @Test
    void get_first_and_last_from_empty_throws() {
        CircularLinkedList<Integer> cll = new CircularLinkedList<>();

        assertThrows(IllegalStateException.class, cll::getFirst);
        assertThrows(IllegalStateException.class, cll::getLast);
    }

    @Test
    void find_existing_elements() {
        CircularLinkedList<String> cll = new CircularLinkedList<>();

        cll.addLast("a");
        cll.addLast("b");
        cll.addLast("c");

        CircularLinkedList.Node<String> nodeB = cll.find("b");
        assertNotNull(nodeB);
        assertEquals("b", nodeB.value);

        CircularLinkedList.Node<String> nodeC = cll.find("c");
        assertNotNull(nodeC);
        assertEquals("c", nodeC.value);
    }

    @Test
    void find_non_existing_element_returns_null() {
        CircularLinkedList<Integer> cll = new CircularLinkedList<>();

        cll.addLast(1);
        cll.addLast(2);
        cll.addLast(3);

        CircularLinkedList.Node<Integer> node = cll.find(99);
        assertNull(node);
    }

    @Test
    void circular_traversal_exactly_one_cycle() {
        CircularLinkedList<Integer> cll = new CircularLinkedList<>();

        cll.addLast(10);
        cll.addLast(20);
        cll.addLast(30);

        CircularLinkedList.Node<Integer> head = cll.tail.next;
        CircularLinkedList.Node<Integer> current = head;

        int[] values = new int[cll.size()];
        int i = 0;

        do {
            values[i++] = current.value;
            current = current.next;
        } while (current != head);

        assertArrayEquals(new int[]{10, 20, 30}, values);
        assertSame(head, current); // after full cycle, we're back at head
    }
}
