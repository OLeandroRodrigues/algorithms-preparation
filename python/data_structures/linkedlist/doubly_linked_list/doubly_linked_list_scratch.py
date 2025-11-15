class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None  # pointer to previous node
        self.next = None  # pointer to next node

    def __repr__(self):
        return f"Node({self.value!r})"


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # ---------- Helpers ----------
    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __repr__(self):
        values = ", ".join(repr(v) for v in self)
        return f"DoublyLinkedList([{values}])"

    # ---------- Core operations ----------
    def push_front(self, x):
        new_node = Node(x)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self._size += 1
        return new_node

    def push_back(self, x):
        new_node = Node(x)

        if self.is_empty():
            # list is empty: head and tail become the new node
            self.head = self.tail = new_node
        else:
            # link new_node after current tail
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1
        return new_node

    def insert_after(self, node, x):
        if node is None:
            raise ValueError("node must not be None")

        if node is self.tail:
            return self.push_back(x)

        new_node = Node(x)

        # link new_node between node and node.next
        successor = node.next
        new_node.prev = node
        new_node.next = successor

        node.next = new_node
        successor.prev = new_node

        self._size += 1
        return new_node

    def insert_before(self, node, x):
        if node is None:
            raise ValueError("node must not be None")

        if node is self.head:
            return self.push_front(x)

        new_node = Node(x)

        predecessor = node.prev
        new_node.next = node
        new_node.prev = predecessor

        predecessor.next = new_node
        node.prev = new_node

        self._size += 1
        return new_node

    def pop_front(self):
        if self.is_empty():
            raise IndexError("pop_front from empty list")

        node = self.head
        value = node.value

        if self.head is self.tail:
            # only one element
            self.head = self.tail = None
        else:
            # move head forward
            self.head = self.head.next
            self.head.prev = None

        self._size -= 1
        return value

    def pop_back(self):
        if self.is_empty():
            raise IndexError("pop_back from empty list")

        node = self.tail
        value = node.value

        if self.head is self.tail:
            # only one element
            self.head = self.tail = None
        else:
            # move tail backward
            self.tail = self.tail.prev
            self.tail.next = None

        self._size -= 1
        return value

    def remove(self, node):
        if node is None:
            raise ValueError("node must not be None")

        if self.is_empty():
            raise IndexError("remove from empty list")

        # If it's the only node
        if node is self.head and node is self.tail:
            self.head = self.tail = None

        # If it's the head (but not the only node)
        elif node is self.head:
            self.head = node.next
            self.head.prev = None

        # If it's the tail (but not the only node)
        elif node is self.tail:
            self.tail = node.prev
            self.tail.next = None

        # Node is in the middle
        else:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node

        # help garbage collector
        node.prev = None
        node.next = None

        self._size -= 1
        return node.value

    def find(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None
