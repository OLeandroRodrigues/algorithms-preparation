
package data_structures.stack;

import org.junit.jupiter.api.Test;
import java.util.NoSuchElementException;

import static org.junit.jupiter.api.Assertions.*;

class StackTest {

    @Test
    void testPushAndPeek() {
        Stack<Integer> stack = new Stack<>();

        assertTrue(stack.isEmpty(), "Stack should start empty");

        stack.push(10);
        stack.push(20);
        stack.push(30);

        assertEquals(3, stack.size());
        assertEquals(30, stack.peek());
        assertFalse(stack.isEmpty());

        System.out.println("testPushAndPeek passed successfully!");
    }

    @Test
    void testPopFollowsLifoOrder() {
        Stack<String> stack = new Stack<>();

        stack.push("A");
        stack.push("B");
        stack.push("C");

        assertEquals("C", stack.pop());
        assertEquals("B", stack.pop());
        assertEquals("A", stack.pop());
        assertTrue(stack.isEmpty());

        System.out.println("testPopFollowsLifoOrder passed successfully!");
    }

    @Test
    void testPeekDoesNotRemoveElement() {
        Stack<Integer> stack = new Stack<>();

        stack.push(99);
        int top = stack.peek();

        assertEquals(99, top);
        assertEquals(1, stack.size());
        assertFalse(stack.isEmpty());

        System.out.println("testPeekDoesNotRemoveElement passed successfully!");
    }

    @Test
    void testPopOnEmptyStackThrows() {
        Stack<Double> stack = new Stack<>();

        assertThrows(NoSuchElementException.class, stack::pop);
        System.out.println("testPopOnEmptyStackThrows passed successfully!");
    }

    @Test
    void testPeekOnEmptyStackThrows() {
        Stack<Integer> stack = new Stack<>();

        assertThrows(NoSuchElementException.class, stack::peek);
        System.out.println("testPeekOnEmptyStackThrows passed successfully!");
    }

    @Test
    void testToStringRepresentation() {
        Stack<Integer> stack = new Stack<>();

        stack.push(1);
        stack.push(2);
        stack.push(3);

        String repr = stack.toString();
        assertTrue(repr.contains("Stack"));
        assertTrue(repr.contains("[1, 2, 3]"));

        System.out.println("testToStringRepresentation passed successfully!");
    }
}
