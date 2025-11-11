package data_structures.stack;

import java.util.ArrayList;
import java.util.NoSuchElementException;

public class Stack<E> {

    private final ArrayList<E> items;

    public Stack() {
        this.items = new ArrayList<>();
    }

    public void push(E item) {
        items.add(item);
    }

    public E pop() {
        if (isEmpty()) {
            throw new NoSuchElementException("pop from empty stack");
        }
        return items.remove(items.size() - 1);
    }

    public E peek() {
        if (isEmpty()) {
            throw new NoSuchElementException("peek from empty stack");
        }
        return items.get(items.size() - 1);
    }

    public boolean isEmpty() {
        return items.isEmpty();
    }

    public int size() {
        return items.size();
    }

    @Override
    public String toString() {
        return "Stack(" + items.toString() + ")";
    }
}
