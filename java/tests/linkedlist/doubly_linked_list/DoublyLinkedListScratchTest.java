package data_structures.linkedlist.doubly_linked_list;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;

import static org.junit.jupiter.api.Assertions.*;

class DoublyLinkedListScratchTest {

    private DoublyLinkedListScratch<Integer> list;

    @BeforeEach
    void setUp() {
        list = new DoublyLinkedListScratch<>();
    }

    private List<Integer> toList(DoublyLinkedListScratch<Integer> lst) {
        List<Integer> result = new ArrayList<>();
        DoublyLinkedListScratch.Node<Integer> current = lst.getHead();
        while (current != null) {
            result.add(current.getValue());
            current = current.getNext();
        }
        return result;
    }

    @Test
    void initialState_shouldBeEmpty() {
        assertTrue(list.isEmpty());
        assertEquals(0, list.size());
        assertNull(list.getHead());
        assertNull(list.getTail());
        assertEquals("DoublyLinkedListScratch[]", list.toString());
    }


    @Test
    void pushFront_onEmptyList_setsHeadAndTail() {
        DoublyLinkedListScratch.Node<Integer> n = list.pushFront(10);

        assertFalse(list.isEmpty());
        assertEquals(1, list.size());
        assertSame(n, list.getHead());
        assertSame(n, list.getTail());
        assertNull(n.getPrev());
        assertNull(n.getNext());
        assertEquals(List.of(10), toList(list));
    }

    @Test
    void pushFront_onNonEmptyList_updatesHead() {
        DoublyLinkedListScratch.Node<Integer> n1 = list.pushFront(10);
        DoublyLinkedListScratch.Node<Integer> n2 = list.pushFront(20);

        assertEquals(2, list.size());
        assertSame(n2, list.getHead());
        assertSame(n1, list.getTail());
        assertNull(n2.getPrev());
        assertSame(n1, n2.getNext());
        assertSame(n2, n1.getPrev());
        assertNull(n1.getNext());

        assertEquals(List.of(20, 10), toList(list));
    }

    @Test
    void pushBack_onEmptyList_setsHeadAndTail() {
        DoublyLinkedListScratch.Node<Integer> n = list.pushBack(10);

        assertFalse(list.isEmpty());
        assertEquals(1, list.size());
        assertSame(n, list.getHead());
        assertSame(n, list.getTail());
        assertNull(n.getPrev());
        assertNull(n.getNext());
        assertEquals(List.of(10), toList(list));
    }

    @Test
    void pushBack_onNonEmptyList_updatesTail() {
        DoublyLinkedListScratch.Node<Integer> n1 = list.pushBack(10);
        DoublyLinkedListScratch.Node<Integer> n2 = list.pushBack(20);

        assertEquals(2, list.size());
        assertSame(n1, list.getHead());
        assertSame(n2, list.getTail());
        assertNull(n1.getPrev());
        assertSame(n2, n1.getNext());
        assertSame(n1, n2.getPrev());
        assertNull(n2.getNext());

        assertEquals(List.of(10, 20), toList(list));
    }

    @Test
    void insertAfter_middleNode_insertsBetweenNodes() {
        DoublyLinkedListScratch.Node<Integer> n1 = list.pushBack(10);
        DoublyLinkedListScratch.Node<Integer> n2 = list.pushBack(20);
        DoublyLinkedListScratch.Node<Integer> n3 = list.pushBack(30);

        DoublyLinkedListScratch.Node<Integer> nNew = list.insertAfter(n1, 15);

        assertEquals(4, list.size());
        assertSame(nNew, n1.getNext());
        assertSame(n1, nNew.getPrev());
        assertSame(n2, nNew.getNext());
        assertSame(nNew, n2.getPrev());

        assertEquals(List.of(10, 15, 20, 30), toList(list));
    }

    @Test
    void insertAfter_tail_delegatesToPushBack() {
        DoublyLinkedListScratch.Node<Integer> n1 = list.pushBack(10);
        DoublyLinkedListScratch.Node<Integer> n2 = list.pushBack(20);

        DoublyLinkedListScratch.Node<Integer> nNew = list.insertAfter(n2, 30);

        assertEquals(3, list.size());
        assertSame(nNew, list.getTail());
        assertEquals(List.of(10, 20, 30), toList(list));
    }

    @Test
    void insertAfter_nullNode_throws() {
        assertThrows(IllegalArgumentException.class,
                () -> list.insertAfter(null, 10));
    }

    @Test
    void insertBefore_middleNode_insertsBetweenNodes() {
        DoublyLinkedListScratch.Node<Integer> n1 = list.pushBack(10);
        DoublyLinkedListScratch.Node<Integer> n2 = list.pushBack(20);
        DoublyLinkedListScratch.Node<Integer> n3 = list.pushBack(30);

        DoublyLinkedListScratch.Node<Integer> nNew = list.insertBefore(n2, 15);

        assertEquals(4, list.size());
        assertSame(nNew, n1.getNext());
        assertSame(n1, nNew.getPrev());
        assertSame(n2, nNew.getNext());
        assertSame(nNew, n2.getPrev());

        assertEquals(List.of(10, 15, 20, 30), toList(list));
    }

    @Test
    void insertBefore_head_delegatesToPushFront() {
        DoublyLinkedListScratch.Node<Integer> n1 = list.pushBack(10);
        DoublyLinkedListScratch.Node<Integer> n2 = list.pushBack(20);

        DoublyLinkedListScratch.Node<Integer> nNew = list.insertBefore(n1, 5);

        assertEquals(3, list.size());
        assertSame(nNew, list.getHead());
        assertEquals(List.of(5, 10, 20), toList(list));
    }

    @Test
    void insertBefore_nullNode_throws() {
        assertThrows(IllegalArgumentException.class,
                () -> list.insertBefore(null, 10));
    }

    @Test
    void popFront_singleElement_clearsList() {
        list.pushBack(10);

        int value = list.popFront();
        assertEquals(10, value);
        assertTrue(list.isEmpty());
        assertNull(list.getHead());
        assertNull(list.getTail());
    }

    @Test
    void popFront_multipleElements_movesHead() {
        list.pushBack(10);
        list.pushBack(20);

        int value = list.popFront();
        assertEquals(10, value);
        assertEquals(1, list.size());
        assertEquals(List.of(20), toList(list));
        assertNull(list.getHead().getPrev());
    }

    @Test
    void popFront_onEmptyList_throws() {
        assertThrows(NoSuchElementException.class,
                list::popFront);
    }

    @Test
    void popBack_singleElement_clearsList() {
        list.pushBack(10);

        int value = list.popBack();
        assertEquals(10, value);
        assertTrue(list.isEmpty());
        assertNull(list.getHead());
        assertNull(list.getTail());
    }

    @Test
    void popBack_multipleElements_movesTail() {
        list.pushBack(10);
        list.pushBack(20);

        int value = list.popBack();
        assertEquals(20, value);
        assertEquals(1, list.size());
        assertEquals(List.of(10), toList(list));
        assertNull(list.getTail().getNext());
    }

    @Test
    void popBack_onEmptyList_throws() {
        assertThrows(NoSuchElementException.class,
                list::popBack);
    }

    @Test
    void remove_singleNode_clearsList() {
        DoublyLinkedListScratch.Node<Integer> n = list.pushBack(10);
        int removed = list.remove(n);

        assertEquals(10, removed);
        assertTrue(list.isEmpty());
        assertNull(list.getHead());
        assertNull(list.getTail());
    }

    @Test
    void remove_headInMultiElementList_updatesHead() {
        DoublyLinkedListScratch.Node<Integer> n1 = list.pushBack(10);
        list.pushBack(20);
        list.pushBack(30);

        int removed = list.remove(n1);
        assertEquals(10, removed);
        assertEquals(2, list.size());
        assertEquals(20, list.getHead().getValue());
        assertNull(list.getHead().getPrev());
        assertEquals(List.of(20, 30), toList(list));
    }

    @Test
    void remove_tailInMultiElementList_updatesTail() {
        list.pushBack(10);
        list.pushBack(20);
        DoublyLinkedListScratch.Node<Integer> n3 = list.pushBack(30);

        int removed = list.remove(n3);
        assertEquals(30, removed);
        assertEquals(2, list.size());
        assertEquals(20, list.getTail().getValue());
        assertNull(list.getTail().getNext());
        assertEquals(List.of(10, 20), toList(list));
    }

    @Test
    void remove_middleNode_linksNeighbors() {
        DoublyLinkedListScratch.Node<Integer> n1 = list.pushBack(10);
        DoublyLinkedListScratch.Node<Integer> n2 = list.pushBack(20);
        DoublyLinkedListScratch.Node<Integer> n3 = list.pushBack(30);

        int removed = list.remove(n2);
        assertEquals(20, removed);
        assertEquals(2, list.size());
        assertSame(n3, n1.getNext());
        assertSame(n1, n3.getPrev());
        assertEquals(List.of(10, 30), toList(list));
    }

    @Test
    void remove_nullNode_throws() {
        assertThrows(IllegalArgumentException.class,
                () -> list.remove(null));
    }

    @Test
    void remove_fromEmptyList_throws() {
        DoublyLinkedListScratch.Node<Integer> fakeNode =
                new DoublyLinkedListScratch.Node<>(10);

        assertThrows(NoSuchElementException.class,
                () -> list.remove(fakeNode));
    }

    @Test
    void find_existingValue_returnsNode() {
        list.pushBack(10);
        list.pushBack(20);
        list.pushBack(30);

        DoublyLinkedListScratch.Node<Integer> found = list.find(20);
        assertNotNull(found);
        assertEquals(20, found.getValue());
    }

    @Test
    void find_missingValue_returnsNull() {
        list.pushBack(10);
        list.pushBack(20);

        DoublyLinkedListScratch.Node<Integer> found = list.find(99);
        assertNull(found);
    }

    @Test
    void toString_containsValuesInOrder() {
        list.pushBack(1);
        list.pushBack(2);
        list.pushBack(3);

        String s = list.toString();
        assertTrue(s.startsWith("DoublyLinkedListScratch["));
        assertTrue(s.contains("1"));
        assertTrue(s.contains("2"));
        assertTrue(s.contains("3"));
    }
}
