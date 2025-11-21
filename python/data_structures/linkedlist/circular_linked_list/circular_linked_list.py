class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.tail = None   # tail.next = head
        self.size = 0

    def is_empty(self):
        return self.tail is None

    def __len__(self):
        return self.size

    
    def add_first(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.tail = new_node
            new_node.next = new_node     # circular: points to itself
        else:
            new_node.next = self.tail.next   # current head
            self.tail.next = new_node        # new_node becomes new head

        self.size += 1

    def add_last(self, value):
        self.add_first(value)
        self.tail = self.tail.next  # move tail to the new node

    def remove_first(self):
        if self.is_empty():
            raise IndexError("remove_first from empty list")

        head = self.tail.next
        value = head.value

        # Only one node
        if self.tail is head:
            self.tail = None
        else:
            self.tail.next = head.next  # bypass the old head

        self.size -= 1
        return value

    def get_first(self):
        if self.is_empty():
            raise IndexError("get_first from empty list")
        return self.tail.next.value  # head

    def get_last(self):
        if self.is_empty():
            raise IndexError("get_last from empty list")
        return self.tail.value

    def find(self, value):
        if self.is_empty():
            return None

        current = self.tail.next  # head

        while True:
            if current.value == value:
                return current
            current = current.next

            if current == self.tail.next:
                break  # completed full cycle

        return None
    
    def __repr__(self):
        if self.is_empty():
            return "CircularLinkedList([])"

        elements = []
        current = self.tail.next  # head

        while True:
            elements.append(repr(current.value))
            current = current.next
            if current == self.tail.next:
                break

        return f"CircularLinkedList([{', '.join(elements)}])"
