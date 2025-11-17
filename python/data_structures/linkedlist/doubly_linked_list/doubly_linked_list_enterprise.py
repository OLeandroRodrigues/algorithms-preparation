from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, Optional, TypeVar

T = TypeVar("T")

@dataclass(slots=True)
class _Node(Generic[T]):
    value: T
    prev: Optional["_Node[T]"] = None
    next: Optional["_Node[T]"] = None

    def __repr__(self) -> str:
        return f"_Node({self.value!r})"


class DoublyLinkedList(Generic[T]):
    """
    A simple doubly linked list implementation.

    Operations:
    - push_front, push_back
    - insert_after, insert_before
    - pop_front, pop_back
    - remove(node)
    - find(value)
    - is_empty, size
    """

    __slots__ = ("_head", "_tail", "_size")

    def __init__(self, values: Optional[Iterable[T]] = None) -> None:
        self._head: Optional[_Node[T]] = None
        self._tail: Optional[_Node[T]] = None
        self._size: int = 0

        if values is not None:
            for v in values:
                self.push_back(v)

    # Basic properties / helpers    
    def is_empty(self) -> bool:
        """Return True if the list has no elements."""
        return self._size == 0

    def size(self) -> int:
        """Return the number of elements in the list."""
        return self._size

    def __len__(self) -> int:  # len(list)
        return self._size

    def __bool__(self) -> bool:  # if list:
        return not self.is_empty()

    @property
    def head(self) -> Optional[_Node[T]]:
        """First node of the list, or None if empty."""
        return self._head

    @property
    def tail(self) -> Optional[_Node[T]]:
        """Last node of the list, or None if empty."""
        return self._tail

    # Core operations
    def push_front(self, value: T) -> _Node[T]:
        """Insert value at the beginning of the list and return the new node."""
        new_node = _Node(value=value, next=self._head)

        if self._head is None:
            # list was empty
            self._tail = new_node
        else:
            self._head.prev = new_node

        self._head = new_node
        self._size += 1
        return new_node

    def push_back(self, value: T) -> _Node[T]:
        """Insert value at the end of the list and return the new node."""
        new_node = _Node(value=value, prev=self._tail)

        if self._tail is None:
            # list was empty
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1
        return new_node

    def insert_after(self, node: _Node[T], value: T) -> _Node[T]:
        """
        Insert value immediately after the given node.

        Raises:
            ValueError: if node is None.
        """
        if node is None:
            raise ValueError("insert_after: node cannot be None")

        if node is self._tail:
            return self.push_back(value)

        successor = node.next
        new_node = _Node(value=value, prev=node, next=successor)

        node.next = new_node
        if successor is not None:
            successor.prev = new_node

        self._size += 1
        return new_node

    def insert_before(self, node: _Node[T], value: T) -> _Node[T]:
        """
        Insert value immediately before the given node.

        Raises:
            ValueError: if node is None.
        """
        if node is None:
            raise ValueError("insert_before: node cannot be None")

        if node is self._head:
            return self.push_front(value)

        predecessor = node.prev
        new_node = _Node(value=value, prev=predecessor, next=node)

        if predecessor is not None:
            predecessor.next = new_node
        node.prev = new_node

        self._size += 1
        return new_node

    def pop_front(self) -> T:
        """
        Remove and return the first element of the list.

        Raises:
            IndexError: if the list is empty.
        """
        if self._head is None:
            raise IndexError("pop_front from empty list")

        node = self._head
        value = node.value

        if self._head is self._tail:
            # single element
            self._head = self._tail = None
        else:
            self._head = self._head.next
            assert self._head is not None  # for type checkers
            self._head.prev = None

        self._size -= 1
        return value

    def pop_back(self) -> T:
        """
        Remove and return the last element of the list.

        Raises:
            IndexError: if the list is empty.
        """
        if self._tail is None:
            raise IndexError("pop_back from empty list")

        node = self._tail
        value = node.value

        if self._head is self._tail:
            self._head = self._tail = None
        else:
            self._tail = self._tail.prev
            assert self._tail is not None
            self._tail.next = None

        self._size -= 1
        return value

    def remove(self, node: _Node[T]) -> T:
        """
        Remove an arbitrary node from the list in O(1).

        Raises:
            ValueError: if node is None.
            IndexError: if the list is empty.
        """
        if node is None:
            raise ValueError("remove: node cannot be None")

        if self.is_empty():
            raise IndexError("remove from empty list")

        if node is self._head and node is self._tail:
            self._head = self._tail = None

        elif node is self._head:
            self._head = node.next
            assert self._head is not None
            self._head.prev = None

        elif node is self._tail:
            self._tail = node.prev
            assert self._tail is not None
            self._tail.next = None

        else:
            prev_node = node.prev
            next_node = node.next
            assert prev_node is not None and next_node is not None
            prev_node.next = next_node
            next_node.prev = prev_node

        # help GC and avoid accidental reuse of pointers
        node.prev = None
        node.next = None

        self._size -= 1
        return node.value

    def find(self, value: T) -> Optional[_Node[T]]:
        """Return the first node whose value == value, or None if not found."""
        current = self._head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def clear(self) -> None:
        """Remove all elements from the list."""
        current = self._head
        while current is not None:
            nxt = current.next
            current.prev = None
            current.next = None
            current = nxt
        self._head = self._tail = None
        self._size = 0

    # Pythonic interfaces
    def __iter__(self) -> Iterator[T]:
        current = self._head
        while current is not None:
            yield current.value
            current = current.next

    def __reversed__(self) -> Iterator[T]:
        current = self._tail
        while current is not None:
            yield current.value
            current = current.prev

    def __contains__(self, value: object) -> bool:
        current = self._head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def __repr__(self) -> str:
        values = ", ".join(repr(v) for v in self)
        return f"DoublyLinkedList([{values}])"
