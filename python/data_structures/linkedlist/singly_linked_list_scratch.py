class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedListScratch:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size_value = 0

    def make_node(self, value):
        return Node(value)

    def push_front(self, value):
        n = self.make_node(value)
        n.next = self.head
        self.head = n

        if self.tail is None:
            self.tail = n

        self.size_value += 1
        return n

    def push_back(self, value):
        n = self.make_node(value)

        if self.tail is None:
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n

        self.size_value += 1
        return n

    def insert_after(self, node, value):
        if node is None:
            raise ValueError("insert_after: node cannot be None")

        n = self.make_node(value)
        n.next = node.next
        node.next = n

        if self.tail is node:
            self.tail = n

        self.size_value += 1
        return n

    def pop_front(self):
        if self.head is None:
            raise IndexError("pop_front from empty list")

        value = self.head.value
        self.head = self.head.next
        self.size_value -= 1

        if self.head is None:
            self.tail = None

        return value

    def remove_after(self, node):
        if node is None or node.next is None:
            raise ValueError("remove_after: nothing to remove")

        to_remove = node.next
        node.next = to_remove.next

        if self.tail is to_remove:
            self.tail = node

        self.size_value -= 1
        return to_remove.value

    def find(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def is_empty(self):
        return self.size_value == 0

    def size(self):
        return self.size_value