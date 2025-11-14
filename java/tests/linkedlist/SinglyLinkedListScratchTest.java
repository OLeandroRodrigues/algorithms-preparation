package data_structures.linkedlist;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class SinglyLinkedListScratchTest {

    @Test
    void testPushFront() {
        SinglyLinkedListScratch list = new SinglyLinkedListScratch();

        list.pushFront(3);  // [3]
        list.pushFront(2);  // [2, 3]
        list.pushFront(1);  // [1, 2, 3]

        assertEquals(3, list.size());
        assertNotNull(list.getHead());
        assertEquals(1, list.getHead().value);
        assertEquals(2, list.getHead().next.value);
        assertNotNull(list.getTail());
        assertEquals(3, list.getTail().value);
    }

    @Test
    void testPushBack() {
        SinglyLinkedListScratch list = new SinglyLinkedListScratch();

        list.pushBack(1);   // [1]
        list.pushBack(2);   // [1, 2]
        list.pushBack(3);   // [1, 2, 3]

        assertEquals(3, list.size());
        assertEquals(1, list.getHead().value);
        assertEquals(3, list.getTail().value);
        assertEquals(2, list.getHead().next.value);
    }

    @Test
    void testInsertAfterMiddle() {
        SinglyLinkedListScratch list = new SinglyLinkedListScratch();

        SinglyLinkedListScratch.Node n1 = list.pushBack(1);
        SinglyLinkedListScratch.Node n2 = list.pushBack(2);
        list.pushBack(4);      // [1, 2, 4]

        list.insertAfter(n2, 3);   // [1, 2, 3, 4]

        assertEquals(4, list.size());
        assertEquals(2, n2.value);
        assertNotNull(n2.next);
        assertEquals(3, n2.next.value);
        assertEquals(4, n2.next.next.value);
    }

    @Test
    void testInsertAfterTailUpdatesTail() {
        SinglyLinkedListScratch list = new SinglyLinkedListScratch();

        list.pushBack(1);
        SinglyLinkedListScratch.Node last = list.pushBack(2);  // tail = 2

        list.insertAfter(last, 3);     // [1, 2, 3]

        assertEquals(3, list.size());
        assertEquals(3, list.getTail().value);
        assertEquals(2, last.value);
        assertEquals(3, last.next.value);
    }

    @Test
    void testPopFront() {
        SinglyLinkedListScratch list = new SinglyLinkedListScratch();

        list.pushBack(10);
        list.pushBack(20);
        list.pushBack(30);    // [10, 20, 30]

        Object value = list.popFront();  // remove 10 -> [20, 30]

        assertEquals(10, value);
        assertEquals(2, list.size());
        assertEquals(20, list.getHead().value);
        assertEquals(30, list.getTail().value);
    }

    @Test
    void testPopFrontUntilEmpty() {
        SinglyLinkedListScratch list = new SinglyLinkedListScratch();

        list.pushBack(1);
        list.pushBack(2);

        assertEquals(1, list.popFront());
        assertEquals(2, list.popFront());
        assertTrue(list.isEmpty());
        assertNull(list.getHead());
        assertNull(list.getTail());
    }

    @Test
    void testPopFrontOnEmptyThrows() {
        SinglyLinkedListScratch list = new SinglyLinkedListScratch();

        assertThrows(RuntimeException.class, list::popFront);
    }

    @Test
    void testRemoveAfterMiddle() {
        SinglyLinkedListScratch list = new SinglyLinkedListScratch();

        SinglyLinkedListScratch.Node n1 = list.pushBack(1);
        SinglyLinkedListScratch.Node n2 = list.pushBack(2);
        list.pushBack(3);   // [1, 2, 3]

        Object removed = list.removeAfter(n1);  // remove 2 -> [1, 3]

        assertEquals(2, removed);
        assertEquals(2, list.size());
        assertEquals(1, list.getHead().value);
        assertEquals(3, list.getHead().next.value);
        assertEquals(3, list.getTail().value);
    }

    @Test
    void testRemoveAfterTailThrows() {
        SinglyLinkedListScratch list = new SinglyLinkedListScratch();

        SinglyLinkedListScratch.Node n1 = list.pushBack(1); // [1]

        assertThrows(IllegalArgumentException.class,
                     () -> list.removeAfter(n1));
    }

    @Test
    void testInsertAfterNullThrows() {
        SinglyLinkedListScratch list = new SinglyLinkedListScratch();

        assertThrows(IllegalArgumentException.class,
                     () -> list.insertAfter(null, 10));
    }

    @Test
    void testFindExistingAndMissing() {
        SinglyLinkedListScratch list = new SinglyLinkedListScratch();

        list.pushBack("A");
        list.pushBack("B");
        list.pushBack("C");

        SinglyLinkedListScratch.Node found = list.find("B");
        assertNotNull(found);
        assertEquals("B", found.value);

        SinglyLinkedListScratch.Node notFound = list.find("X");
        assertNull(notFound);
    }

    @Test
    void testIsEmptyAndSize() {
        SinglyLinkedListScratch list = new SinglyLinkedListScratch();

        assertTrue(list.isEmpty());
        assertEquals(0, list.size());

        list.pushBack(1);
        list.pushBack(2);

        assertFalse(list.isEmpty());
        assertEquals(2, list.size());
    }
}