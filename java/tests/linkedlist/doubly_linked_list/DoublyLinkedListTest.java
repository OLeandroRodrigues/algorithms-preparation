package data_structures.linkedlist.doubly_linked_list;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;

import static org.junit.jupiter.api.Assertions.*;

class DoublyLinkedListTest {

    // ----------------- Helpers -----------------

    private static <T> List<T> toList(DoublyLinkedList<T> list) {
        List<T> result = new ArrayList<>();
        for (T v : list) {
            result.add(v);
        }
        return result;
    }

    private static <T> List<T> toReversedList(DoublyLinkedList<T> list) {
        List<T> result = new ArrayList<>();
        for (T v : list.descendingIterable()) {
            result.add(v);
        }
        return result;
    }

    // ----------------- Estado inicial / básico -----------------

    @Test
    void newList_shouldBeEmpty() {
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();

        assertTrue(list.isEmpty());
        assertEquals(0, list.size());
        assertNull(list.peekFirst());
        assertNull(list.peekLast());
        assertEquals(List.of(), toList(list));
        assertEquals("DoublyLinkedList[]", list.toString());
    }

    @Test
    void constructorWithIterable_populatesList() {
        DoublyLinkedList<Integer> list =
                new DoublyLinkedList<>(List.of(1, 2, 3));

        assertFalse(list.isEmpty());
        assertEquals(3, list.size());
        assertEquals(List.of(1, 2, 3), toList(list));
    }

    // ----------------- addFirst / addLast -----------------

    @Test
    void addFirst_addLast_buildsCorrectOrder() {
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();

        list.addFirst(2);   // [2]
        list.addFirst(1);   // [1, 2]
        list.addLast(3);    // [1, 2, 3]
        list.addLast(4);    // [1, 2, 3, 4]

        assertEquals(4, list.size());
        assertEquals(List.of(1, 2, 3, 4), toList(list));
        assertEquals(1, list.peekFirst());
        assertEquals(4, list.peekLast());
    }

    // ----------------- removeFirst / removeLast -----------------

    @Test
    void removeFirst_onSingleElement_clearsList() {
        DoublyLinkedList<String> list = new DoublyLinkedList<>();
        list.addLast("only");

        String removed = list.removeFirst();

        assertEquals("only", removed);
        assertTrue(list.isEmpty());
        assertNull(list.peekFirst());
        assertNull(list.peekLast());
    }

    @Test
    void removeLast_onSingleElement_clearsList() {
        DoublyLinkedList<String> list = new DoublyLinkedList<>();
        list.addFirst("only");

        String removed = list.removeLast();

        assertEquals("only", removed);
        assertTrue(list.isEmpty());
        assertNull(list.peekFirst());
        assertNull(list.peekLast());
    }

    @Test
    void removeFirst_onMultiElement_movesHead() {
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);

        int r1 = list.removeFirst();
        int r2 = list.removeFirst();

        assertEquals(1, r1);
        assertEquals(2, r2);
        assertEquals(1, list.size());
        assertEquals(List.of(3), toList(list));
        assertEquals(3, list.peekFirst());
        assertEquals(3, list.peekLast());
    }

    @Test
    void removeLast_onMultiElement_movesTail() {
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);

        int r1 = list.removeLast();
        int r2 = list.removeLast();

        assertEquals(3, r1);
        assertEquals(2, r2);
        assertEquals(1, list.size());
        assertEquals(List.of(1), toList(list));
        assertEquals(1, list.peekFirst());
        assertEquals(1, list.peekLast());
    }

    @Test
    void removeFirst_onEmpty_throws() {
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();

        assertThrows(NoSuchElementException.class, list::removeFirst);
    }

    @Test
    void removeLast_onEmpty_throws() {
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();

        assertThrows(NoSuchElementException.class, list::removeLast);
    }

    // ----------------- peekFirst / peekLast -----------------

    @Test
    void peekFirst_peekLast_doNotModifyList() {
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();
        list.addLast(10);
        list.addLast(20);

        Integer first = list.peekFirst();
        Integer last = list.peekLast();

        assertEquals(10, first);
        assertEquals(20, last);
        assertEquals(2, list.size());
        assertEquals(List.of(10, 20), toList(list));
    }

    @Test
    void peek_onEmpty_returnsNull() {
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();

        assertNull(list.peekFirst());
        assertNull(list.peekLast());
    }

    // ----------------- contains / removeFirstOccurrence -----------------

    @Test
    void contains_and_removeFirstOccurrence_workAsExpected() {
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();
        list.addLast(1);
        list.addLast(2);
        list.addLast(2);
        list.addLast(3);

        assertTrue(list.contains(2));
        assertTrue(list.removeFirstOccurrence(2)); // remove a primeira ocorrência

        assertEquals(List.of(1, 2, 3), toList(list));
        assertTrue(list.contains(2));

        assertTrue(list.removeFirstOccurrence(2)); // remove a segunda
        assertEquals(List.of(1, 3), toList(list));
        assertFalse(list.contains(2));

        assertFalse(list.removeFirstOccurrence(2)); // nada a remover
    }

    @Test
    void contains_handlesNullCorrectly() {
        DoublyLinkedList<String> list = new DoublyLinkedList<>();
        list.addLast(null);
        list.addLast("a");

        assertTrue(list.contains(null));
        assertTrue(list.removeFirstOccurrence(null));
        assertFalse(list.contains(null));
        assertEquals(List.of("a"), toList(list));
    }

    // ----------------- clear -----------------

    @Test
    void clear_emptiesList() {
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);

        list.clear();

        assertTrue(list.isEmpty());
        assertEquals(0, list.size());
        assertEquals(List.of(), toList(list));
        assertNull(list.peekFirst());
        assertNull(list.peekLast());
    }

    // ----------------- iteration -----------------

    @Test
    void iterator_traversesInInsertionOrder() {
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);

        assertEquals(List.of(1, 2, 3), toList(list));
    }

    @Test
    void descendingIterable_traversesInReverseOrder() {
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);

        assertEquals(List.of(3, 2, 1), toReversedList(list));
    }

    @Test
    void iterator_remove_removesCurrentElement() {
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);

        var it = list.iterator();
        assertEquals(1, it.next());
        it.remove(); // remove o 1
        assertEquals(2, it.next());
        assertEquals(3, it.next());

        assertEquals(List.of(2, 3), toList(list));
        assertEquals(2, list.size());
    }

    // ----------------- toString -----------------

    @Test
    void toString_containsValuesInOrder() {
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);

        String s = list.toString();
        assertTrue(s.startsWith("DoublyLinkedList["));
        assertTrue(s.contains("1"));
        assertTrue(s.contains("2"));
        assertTrue(s.contains("3"));
        assertTrue(s.endsWith("]"));
    }
}
